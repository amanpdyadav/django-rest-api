from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from authentication.authentication import isAuthenticated
from models import Events
from tnaapp.helper_functions import JSONResponse, notlogged
from tnaapp.homeview import getEvents


def updateEvent(request):
    res = JSONParser().parse(request)
    event = Events.objects.get(id=res['id'])
    event.registration_open = False

    res = JSONParser().parse(request)
    if 'title' in res:
        event.title = str(res['title'])

    if 'description' in res:
        event.description = str(res['description'])

    if 'location' in res:
        event.location = str(res['location'])

    if 'datetime' in res:
        event.datetime = str(res['datetime'])

    if 'adult_price' in res:
        event.adult_price = int(res['adult_price'])

    if 'family_price' in res:
        event.family_price = int(res['family_price'])

    if 'children_price' in res:
        event.children_price = int(res['children_price'])

    if 'reference_number' in res:
        reference_number = str(res['reference_number'])
        event.reference_number = reference_number

    try:
        registration = True
        expiry_datetime = str(res['expiry_datetime'])
        if datetime.now() < datetime.strptime(expiry_datetime, '%Y-%m-%d %H:%M'):
            event.registration_open = True
        if res['registration'] and (int(res['adult_price']) < 1 or int(res['family_price']) < 1):
            return JSONResponse({'message': "You need to set the price for adults and family both" }, status=400)
    except:
        registration = False
        expiry_datetime = datetime.now()
    event.registration = registration
    event.expiry_datetime = expiry_datetime
    try:
        event.save()
    except:
        return JSONResponse({'message': "Not a valid date time." }, status=400)
    return JSONResponse({"events": getEvents()}, status=200)


def addEvent(request, authMember):
    res = JSONParser().parse(request)
    reference_number = ""
    if res['reference_number']:
        reference_number = str(res['reference_number'])
    try:
        registration = True
        registration_open = True
        expiry_datetime = str(res['expiry_datetime'])
        if res['registration'] and (res['adult_price'] < 1 or res['family_price'] < 1):
            return JSONResponse({'message': "You need to set the price for adults and family both" }, status=400)
    except:
        registration = False
        registration_open = False
    try:
        Events(
            owner=authMember,
            title=res['title'],
            description=res['description'].replace('\n', '<br>'),
            location=res['location'],
            datetime=res['datetime'],
            adult_price=res['adult_price'],
            children_price=res['children_price'],
            family_price=res['family_price'],
            registration=registration,
            registration_open=registration_open,
            reference_number=reference_number,
            expiry_datetime=expiry_datetime
        ).save()
    except:
        return JSONResponse({'message': "Not a valid date time." }, status=400)
    return JSONResponse({"events": getEvents() }, status=200)



@csrf_exempt
def eventsHandler(request):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        if request.method == 'PUT':
            return addEvent(request, authMember)
        elif request.method == 'POST':
            return updateEvent(request)

        elif request.method == 'DELETE':
            res = JSONParser().parse(request)
            try:
                evt = Events.objects.get(id=res['id'], owner=authMember)
                evt.delete()
                return JSONResponse({'events': getEvents()}, status=200)
            except:
                return JSONResponse({"message": "Your are not the owner of "
                                                "this event."}, status=400)