from datetime import datetime

from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule

from models import Events, EventAttendees, Member


class ValidateEvent(CronJobBase):
    schedule = Schedule(run_every_mins=1,retry_after_failure_mins=1)
    code = 'tnaapp.cronjob'    # a unique code

    def do(self):
        checkEvents()
        reminderMail()


def checkEvents():
    evt = Events.objects.all()
    for e in evt:
        if datetime.now() > e.expiry_datetime:
            e.registration_open = False
            e.save()


def reminderMail():
    events = Events.objects.all()
    for evt in events:
        evt_atten = EventAttendees.objects.filter(events=evt)
        if diff_dates(evt.expiry_datetime, datetime.now()) <= 2:
            for ea in evt_atten:
                discount = 0
                try:
                    mem = Member.objects.get(email=ea.email)
                    if mem.is_verified:
                        discount = 10
                except:
                    discount = 0

                # Get Rid of encoding in title
                try:
                    title = evt.title
                except:
                    title = ""

                subject = "Event registration payment reminder!"
                message = "Hello " + ea.name + ",\n"\
                          "Please ignore this message if you have already paid. \n\n" \
                          "Event payment due date is about to expire in 2 days. So if you haven't paid for it please do it asap.\n\n" \
                          "In case you want to cancel your participation. " \
                                                   "Please send us a cancellation email or we will be sending you a bill in case you appear or remain absent during the event.\n\n" \
                          + title + "\n\n" \
                          "Invoice details:\n" + \
                          "No. of Adults :" + str(ea.no_adults) + " * " + str(evt.adult_price) + "\n" \
                          "No. of Family : " + str(ea.no_family) + " * " + str(evt.family_price) + "\n" \
                          "No. of Children above 10 years : " + str(ea.no_children) + "\n" \
                          "No. of Vegetarian : " + str(ea.no_vegetarian) + " * " + str(evt.adult_price) + "\n\n" \
                          "Membership Discount " + str(discount) + "%\n\n" \
                          "Total :" + str(float(ea.total) - (float(ea.total) * discount / 100.0)) + " euros \n\n\n" \
                          "Receiver : Turku Nepal Association RY \n" \
                          "Account No : FI6517433000015861 \n" + \
                          str(evt.reference_number) + " (Please do not forget to put in the message.)\n" \
                          "Due Date : " + str(evt.expiry_datetime) + "\n\n" \
                          "Your Sincerely," + "\n" \
                          "Turku Nepali Association ry."

                from_email = "turkunepal@gmail.com"
                to_email = [str(ea.email)]
                if not ea.email_reminder_sent:
                    send_mail(subject, message, from_email, to_email, fail_silently=True)
                    ea.email_reminder_sent = True
                    ea.save()


def diff_dates(date1, date2):
    return (date1-date2).days
