# -*- coding: utf-8 -*-
import codecs
import re

from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

from authentication.authentication import isAuthenticated
from models import Account, AccountFile, Member, EventAttendees
from tna.settings import MEDIA_ROOT
from tnaapp.helper_functions import JSONResponse, notlogged
from tnaapp.homeview import getAccounts


@csrf_exempt
def upload(request):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        files = request.FILES.getlist("files")
        if len(files) > 0:
                for file in files:
                    acc = AccountFile(url=file)
                    acc.save()
                    updateTNAAccountTable(acc.url)
                    default_storage.delete(MEDIA_ROOT + '/' + str(acc.url))
                return JSONResponse({"account": getAccounts()}, status=200)

        else:
            return JSONResponse({'msg': "No files found"}, status=200)


data = []

#Accept TNA Bank format of PRN
def updateTNAAccountTable(file):
    with codecs.open(MEDIA_ROOT + '/' + str(file), "r", encoding="ISO-8859-1") as f:
        dateAmount_regex = r"(?P<day>\d{2}).(?P<month>\d{2}).\s*(\d+)\s*__________ \s*(?P<amount>(\d*,\d+)[-+])"
        beneficiary_regrex = r"(?P<beneficiary>(\w+)(.*?))\s*/[A-Z] "
        ref_num_regrex = r"(\w+)\s*(?P<ref_num>\d{20}(?!\d))"
        year_regrex = r"Entry date\s*(\d+).(\d+).(?P<year>\d{2})"

        year = ''; month = ''; day = ''; amount = ''; ref_num = ''; beneficiary = ''
        for line in f:
            if re.search(year_regrex, line):
                year = '20' + str(re.search(year_regrex, line).group('year'))

            if re.search(dateAmount_regex, line):
                month = str(re.search(dateAmount_regex, line).group("month"))
                day = str(re.search(dateAmount_regex, line).group("day"))
                amount = str(re.search(dateAmount_regex, line).group("amount"))

            if re.search(beneficiary_regrex, line):
                beneficiary = str(re.search(beneficiary_regrex, line).group('beneficiary'))

            if re.search(ref_num_regrex, line):
                ref_num = str(re.search(ref_num_regrex, line).group('ref_num'))[-4::]

            if year and month and day and amount and beneficiary:
                try:
                    acc_exist = Account.objects.filter(year=year, month=month, day=day, amount=amount, beneficiary=beneficiary)
                except:
                    acc_exist = []

                if len(acc_exist) == 0:
                    Account(year=year, month=month, day=day, amount=amount, beneficiary=beneficiary, ref_num=ref_num).save()
                month = ''; day = ''; amount = ''; ref_num = ''; beneficiary = ''




def verifyMember(request, mem_id):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        mem = Member.objects.get(id=mem_id)
        if authMember.is_board_member:
            mem.is_verified = True
            mem.save()
        return JSONResponse({"member": "Update successful."}, status=200)


def verifyEventPayment(request, attendee_id):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        attendee = EventAttendees.objects.get(id=attendee_id)
        if authMember.is_board_member:
            attendee.has_paid = True
            attendee.save()
        return JSONResponse({"member": "Payment successful."}, status=200)

