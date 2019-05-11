# -*- coding: utf-8 -*-
import json
import logging

from rest_framework.decorators import api_view
from django.core.serializers import serialize

from authentication.authentication import user_authenticate
from tnaapp.helper_functions import JSONResponse, getCleanObject


@api_view(['POST'])
def login(request):
    (token, member) = user_authenticate(request)
    logging.info("ID = %s\nTOKEN = %s" % (str(id), str(token)))
    if token:
        return JSONResponse(
            {'msg': "Login Successful.", 'token': 'Bearer ' + token,
             'user': getCleanObject(json.loads(serialize('json', [member])))[0]},
            status=200)
    else:
        return JSONResponse({'msg': "Invalid Username/Password"}, status=401)
