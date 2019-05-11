# -*- coding: utf-8 -*-
import json
import logging

from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from authentication.authentication import isAuthenticated
from models import Info
from serializers.serializers import InfoSerializer
from tnaapp.helper_functions import JSONResponse, reportError, notlogged, \
    getCleanObject
from tnaapp.homeview import getInfos


def addInfo(request):
    try:
        data = JSONParser().parse(request)
        serializer = InfoSerializer(data=data)

        # This is to register the info.
        if serializer.is_valid():
            serializer.save()
            # print serialize('json', [info])
            return JSONResponse({'infos': getInfos()},  status=201)
        else:
            return JSONResponse(serializer.errors, status=400)
    except:
        logging.error("Registration failed: {}".format(reportError()))
        return JSONResponse({'msg': "Some error occured"}, status=400)


def updateInfo(request, authMember):
    try:
        body = JSONParser().parse(request)
        infoQuerySet = Info.objects.filter(id=body['id'], owner=authMember)
        infoQuerySet.update(**body)
        return JSONResponse(getCleanObject(json.loads(serialize('json', infoQuerySet))), status=200)
    except:
        logging.error("Update info failed: {}".format(reportError()))
        return JSONResponse(reportError(), status=400)


@csrf_exempt
def infoHandler(request):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        if request.method == 'PUT':
            return addInfo(request, authMember)
        elif request.method == 'POST':
            return updateInfo(request)

        elif request.method == 'DELETE':
            res = JSONParser().parse(request)
            try:
                inf = Info.objects.get(id=res['id'], owner=authMember)
                inf.delete()
                return JSONResponse({'events': getInfos()}, status=200)
            except:
                return JSONResponse({"message": "Your are not the owner of "
                                                "this event."}, status=400)