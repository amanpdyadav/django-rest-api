# -*- coding: utf-8 -*-
import binascii
import json
import os
import sys
from tna.settings import FRONT_END_URL
from datetime import datetime
from django.core.serializers import serialize

from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from authentication.authentication import getUserWithToken, getJWTToken
from cronjob import diff_dates
from models import ProfilePictures, Events, Member
from tna.settings import MEDIA_ROOT


def notlogged():
    return JSONResponse({'msg': "You are not logged in or the token has expired. Please login again."}, status=401)


def sendEmailVerification(memberid, email, token, request, updated=False):
    emailLink = FRONT_END_URL + "verifyemail/{}/".format(token)
    emailView(email, 'TNA account verification',
              'Please use the following link to verify your email address and verify your account.\n'
              '{}'.format(emailLink))


def emailView(toEmail, subject, body):
    from_email = 'turkunepal@gmail.com'
    send_mail(subject, body, from_email, [toEmail], fail_silently=False)


@csrf_exempt
def resendVerification(request):
    try:
        authToken = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        mem = Member.objects.get(token=authToken)
    except:
        return JSONResponse({'msg': "Not a valid token"}, status=400)

    member = getUserWithToken(authToken)
    uniq_key = binascii.b2a_hex(os.urandom(12))
    member.is_active = False
    member.ev_token = uniq_key
    member.save()
    sendEmailVerification(member.id, member.email, uniq_key, request)
    return JSONResponse({'message': "Email verification sent please check your "
                                    "email Inbox or Spam folder to verify."},
                        status=200)


@csrf_exempt
def emailVerification(request, ev_token):
    try:
        mem = Member.objects.get(ev_token=ev_token)
        mem.is_active = True
        mem.ev_token = ""
        mem.save()
        print json.loads(serialize('json', [mem]))
        return JSONResponse(getCleanObject(json.loads(serialize('json', [mem])))[0], status=200)
    except:
        return JSONResponse({'message': reportError()}, status=400)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def delteEmptydir():
    for root, dirs, files in os.walk(MEDIA_ROOT):
        for d in dirs:
            dir = os.path.join(root, d)
            # check if dir is empty
            if not os.listdir(dir):
                os.rmdir(dir)


def reportError():
    type, value, traceback = sys.exc_info()
    return str(value)


def getProfilePic(request):
    try:
        authToken = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        mem = Member.objects.get(token=authToken)
        return ProfilePictures.objects.get(owner=mem).url
    except:
        return ""


def get_first_name(fullname):
    firstname = ''
    try:
        firstname = fullname.split()[0]
    except Exception as e:
        print str(e)
    return firstname


def get_last_name(fullname):
    lastname = ''
    try:
        index = 0
        for part in fullname.split():
            if index > 0:
                if index > 1:
                    lastname += ' '
                lastname += part
            index += 1
    except Exception as e:
        print str(e)
    return lastname


def get_last_word(string):
    return string.split()[-1]


def get_upcoming_event():
    evt = Events.objects.all()
    upcomintEvt = []
    for e in evt:
        print diff_dates(e.datetime, datetime.now())
        if diff_dates(e.datetime, datetime.now()) >= 0:
            record = {
                "title": e.title,
                "datetime": e.datetime
            }
            upcomintEvt.append(record)
    return upcomintEvt


def getCleanObject(pics):
    temppics = []
    for p in pics:
        p['fields']['pk'] = p['pk']
        temppics.append(p['fields'])
    return temppics
