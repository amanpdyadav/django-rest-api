# -*- coding: utf-8 -*-
import binascii
import logging
import os
from tna.settings import FRONT_END_URL

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from authentication.passwordHasher import hashpassword
from helper_functions import emailView, reportError, JSONResponse
from models import Member


@csrf_exempt
def passwordResetRequest(request):
    if request.method == 'POST':
        email = JSONParser().parse(request)['email']
        try:
            member = Member.objects.get(email=email)
            member.pr_token = str(member.id) + binascii.b2a_hex(os.urandom(12))
            member.save()
            emailLink = FRONT_END_URL + "resetpassword/{}/".format(member.pr_token)
            emailView(email, 'TNA Password Reset Request.',
                      'Please ignore this email if you haven\'t requested to reset your password. '
                      'If you want to reset your password, please follow the link below: \n{}'.format(emailLink))
            return JSONResponse({"message": 'Password link successfully sent. '
                                        'Check your email.'}, status=200)

        except:
            logging.error("Password reset request failed: {}".format(reportError()))
            return JSONResponse({"message": "Password reset request failed: {}".format(reportError())}, status=400)

@csrf_exempt
def passwordReset(request, pr_token):
    if request.method == 'POST' and pr_token != "":
        try:
            password = JSONParser().parse(request)['password']
            print password
            member = Member.objects.get(pr_token=pr_token)
            if not member:
                return JSONResponse({"message": "Please use password request url to generate the password reset link."}, status=400)
            member.password = hashpassword(password)
            member.pr_token = ""
            member.save()
            return JSONResponse({"message": "Password has been successfully "
                                            "changed."}, status=200)

        except:
            logging.error("Password reset failed: {}".format(reportError()))
            return JSONResponse(reportError(), status=404)
