# -*- coding: utf-8 -*-
import json

from django.core.serializers import serialize

from authentication.authentication import isAuthenticated
from models import Member, Info, Events, Gallery, ProfilePictures, \
    GalleryPictures, InfoPictures, EventsPictures, EventAttendees, Account
from tnaapp.helper_functions import JSONResponse, getCleanObject
from tna.settings import BACK_END_URL


def getMembers():
    members = json.loads(serialize('json', Member.objects.all()))
    for mem in members:
        del mem['fields']['token']
        del mem['fields']['password']
        pics = json.loads(serialize('json', ProfilePictures.objects.filter(owner=mem['pk'])))
        if len(pics) > 0:
            mem['fields']['profilepicture'] = pics[0]['fields']['url']
    return getCleanObject(members)


def getInfos():
    infos = json.loads(serialize('json', Info.objects.all()))
    for info in infos:
        pics = json.loads(serialize('json', InfoPictures.objects.filter(info=info['pk'])))
        info['fields']['pictures'] = getCleanObject(pics)
    return getCleanObject(infos)


def getEvents():
    events = json.loads(serialize('json', Events.objects.all()))
    for event in events:
        pics = json.loads(serialize('json', EventsPictures.objects.filter(events=event['pk'])))
        event['fields']['pictures'] = getCleanObject(pics)
    return getCleanObject(events)


def getGalleries():
    galleries = json.loads(serialize('json', Gallery.objects.all()))
    for gallery in galleries:
        pics = json.loads(serialize('json', GalleryPictures.objects.filter(gallery=gallery['pk'])))
        gallery['fields']['pictures'] = getCleanObject(pics)
    return getCleanObject(galleries)


def getEventAttendees():
    return getCleanObject(json.loads(serialize('json', EventAttendees.objects.all())))


def getAccounts():
    return getCleanObject(json.loads(serialize('json', Account.objects.all())))


def getAllData(request):
    data = {
        'member': getMembers(),
        'infos': getInfos(),
        'events': getEvents(),
        'gallery': getGalleries(),
        'eventAttendees': getEventAttendees()
    }
    authMember = isAuthenticated(request)
    if authMember:
        data['accounts'] = getAccounts()
        data['user'] = getCleanObject(json.loads(serialize('json', [authMember])))[0]
        pics = json.loads(serialize('json', ProfilePictures.objects.filter(owner=authMember.id)))
        data['user']['profilepicture'] = ''
        if len(pics) > 0:
            data['user']['profilepicture'] = pics[0]['fields']['url']
    return JSONResponse(data, status=200)