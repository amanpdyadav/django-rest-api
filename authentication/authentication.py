import binascii
import json
import logging
import os
import sys

import jwt
from django.core.serializers import serialize
from rest_framework.parsers import JSONParser

from passwordHasher import passwordCorrect
from tna.settings import JWT_SECRET_KEY
from tnaapp.models import Member


def return_user_authenticate(member):
    member.token = getJWTToken(json.loads(serialize('json', [member]))[0])
    member.save()
    return member.token, member


def user_authenticate(request):
    try:
        res = JSONParser().parse(request)
        if res["username"] != "" and res["password"] != "":
            email = (res["username"]).lower()
            member = Member.objects.get(email=email)
            if passwordCorrect(res["password"].encode('utf-8'), member.password.encode('utf-8')):
                return return_user_authenticate(member)
        return False, id
    except:
        logging.error("Authentication Error {}".format(sys.exc_info()[1]))
        return False, id


def getHEXtoken():
    return binascii.b2a_hex(os.urandom(15))


def getUserWithToken(token):
    return Member.objects.get(token=token)

def getJWTToken(payload):
    try:
        if 'token' in payload['fields']:
            del payload['fields']['token']
        if 'password' in payload:
            del payload['fields']['password']
    except:
        ""
    return jwt.encode(payload, JWT_SECRET_KEY)

def isAuthenticated(request):
    try:
        authToken = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        authMember = Member.objects.get(token=authToken)
        return authMember
    except:
        return False
