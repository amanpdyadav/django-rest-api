# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from models import EventAttendees, Events, Member
from tnaapp.helper_functions import JSONResponse
from tnaapp.homeview import getEventAttendees

@csrf_exempt
def registrationForEvent(request, event_id):
    evt = Events.objects.get(id=event_id)
    if request.method == "POST":
        res = JSONParser().parse(request)
        try:
            total = int(res['no_adults']) * evt.adult_price \
                    + int(res['no_family']) * evt.family_price \
                    + int(res['no_children']) * evt.children_price
        except:
            total = 0
        if res['name'] is not None and res['address'] is not None and res['email'] is not None:
            try:
                attendies_exists = EventAttendees.objects.filter(
                    email=res['email'], events=evt)
                if len(attendies_exists) !=0:
                    return JSONResponse({'message': "You have already registered"
                                                    " for this event. Please contact admin for changes.!!"}, status=400)
                try:
                    mem = Member.objects.get(email=res['email'])
                    if mem.is_verified:
                        total = str(total - total / 10.0)
                        totalMessage = "You have a paid membership discount of 10%.\n" \
                                       "Total :" + total + " euros \n\n\n"
                    else:
                        totalMessage = "Total :" + str(total) + " euros \n\n\n"
                except:
                    totalMessage = "Total :" + str(total) + " euros \n\n\n"
                attendies = EventAttendees(
                    name=res['name'],
                    phone=res['phone'],
                    address=res['address'],
                    email=res['email'],
                    no_adults=res['no_adults'],
                    no_family=res['no_family'],
                    no_children=res['no_children'],
                    no_vegetarian=res['no_vegetarian'],
                    total=total)
                attendies.events = evt
                attendies.save()
                subject = "Event registration successful!"
                message = "Thank you " + res['name'] + ",\n" \
                          "You have been registered for the upcoming event. \n\n" \
                           + (evt.title) + "\n\n" \
                          "Invoice details:\n" + \
                          "No. of Adults :" + str(res['no_adults']) + "\n" \
                          "No. of Family : " + str(res['no_family']) + "\n" \
                          "No. of Children above 10 years : " + str(res['no_children']) + "\n" \
                          "No. of Vegetarian : " + str(res['no_vegetarian']) + "\n\n" \
                          + totalMessage + \
                          "Receiver : Turku Nepal Association RY \n" \
                          "Account No : FI6517433000015861 \n" + str(evt.reference_number) \
                          + " (Please do not forget to put the message)\n" \
                          "Due Date : " + str(evt.expiry_datetime) + "\n\n" \
                          "Your Sincerely," + "\n" \
                          "Turku Nepali Association ry."

                from_email = "turkunepal@gmail.com"
                to_email = [res['email']]
                send_mail(subject, message, from_email, to_email, fail_silently=True)
                return JSONResponse({'eventAttendees': getEventAttendees()}, status=200)
            except:
                return JSONResponse({'message': "Please check the details!!"}, status=400)
