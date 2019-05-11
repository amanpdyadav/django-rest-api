# -*- coding: utf-8 -*-
import binascii
import json
import logging
import os

from django.core.files.storage import default_storage
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from authentication.authentication import getJWTToken, isAuthenticated
from authentication.passwordHasher import hashpassword
from jsonResponse import JSONResponse
# Rest api
from models import Member, ProfilePictures
from serializers.serializers import MemberSerializer
from tna.settings import MEDIA_ROOT
from tnaapp.helper_functions import reportError, sendEmailVerification, \
    notlogged, getCleanObject
from tnaapp.homeview import getMembers


def addMember(request):
    try:
        data = JSONParser().parse(request)
        data['token'] = getJWTToken(data)
        if "email" in data and data["email"] is not "":
            data["email"] = data["email"].lower()
            if Member.objects.filter(email=data["email"]).exists():
                raise ValueError(
                    "Email already exists: {}".format(data["email"]))
        else:
            raise ValueError("Email cannot be empty")

        serializer = MemberSerializer(data=data)

        # This is to register the mem.
        if serializer.is_valid():
            serializer.save()
            mem = Member.objects.get(id=serializer.data['id'])
            mem.ev_token = str(mem.id) + binascii.b2a_hex(os.urandom(12))
            mem.save()
            # print serialize('json', [mem])
            sendEmailVerification(mem.id, mem.email, mem.ev_token, request)
            return JSONResponse(getCleanObject(json.loads(serialize('json', [mem]))), status=201)
        else:
            return JSONResponse(serializer.errors, status=400)
    except ValueError:
        logging.error("Registration failed: {}".format(reportError()))
        return JSONResponse(reportError(), status=400)
    except:
        logging.error("Registration failed: {}".format(reportError()))
        return JSONResponse({'msg': "Some error occured"}, status=400)


def updateMember(request, authMember):
    try:
        body = JSONParser().parse(request)
        # Body contains no information about fields to update.
        if len(body.keys()) < 1:
            return JSONResponse({'msg': 'There is nothing to update'},
                                status=200)

        # Removes the read only fields from body if exists.
        if 'id' in body.keys():
            body.pop('id')
        if 'token' in body.keys():
            body.pop('token')
        if "is_active" in body.keys():
            body.pop("is_active")
        if "is_verified" in body.keys():
            body.pop("is_verified")

        if authMember.email is not "" and "email" in body.keys() and \
                        authMember.email == body["email"].lower():
            del body["email"]

        sendEmail = False
        if "email" in body.keys() and body["email"] is not "":
            body["email"] = body["email"].lower()
            if Member.objects.filter(email=body["email"]).exists():
                raise ValueError(
                    "Email already exists: {}".format(body["email"]))
            else:
                body["is_active"] = False
                body["ev_token"] = str(authMember.id) + binascii.b2a_hex(
                    os.urandom(12))
                sendEmail = True

        # Hash the password before update.
        if 'password' in body.keys():
            body['password'] = hashpassword(body['password'])

        # Finally mem's remaining provided fields will be updated if provided.
        memQuerySet = Member.objects.filter(token=authMember.token)
        memQuerySet.update(**body)
        if sendEmail:
            sendEmailVerification(authMember.id, body["email"], body["ev_token"], request)

        return JSONResponse(getCleanObject(json.loads(serialize('json', memQuerySet))), status=200)
    except:
        logging.error("Update mem failed: {}".format(reportError()))
        return JSONResponse(reportError(), status=400)

@csrf_exempt
def uploadProfilePic(request):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        if request.method == 'POST':
            if len(request.FILES) > 0:
                for i in request.FILES:
                    file = request.FILES[i]
                    try:
                        pic = ProfilePictures.objects.get(owner=authMember)
                        default_storage.delete(MEDIA_ROOT + '/' + str(pic.url))
                        pic.url = file
                        pic.save()
                    except:
                        ProfilePictures(url=file, owner=authMember).save()

        return JSONResponse(getCleanObject(json.loads(serialize('json', [authMember]))), status=200)


@csrf_exempt
def memberHandler(request):
    if request.method == 'PUT':
        return addMember(request)

    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        if request.method == 'POST':
            return updateMember(request, authMember)
        if request.method == 'DELETE':
            authMember.delete()
            return JSONResponse(getMembers(), status=200)