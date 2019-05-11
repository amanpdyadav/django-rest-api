# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from tnaapp.helper_functions import emailView, JSONResponse

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name'] or ''
        email = data['email']
        phone = data['phone'] or ''
        subject = data['subject'] or ''
        message = data['message'] or ''
        emailView(email, "Copy of contact request.", "From {0},\n{1}\n{2}\n{3}".format(name, subject, message, phone))
        emailView("turkunepal@gmail.com", "Contact Request.",
                  "From {0},\nSender email = {1}\n{2}\n{3}\n\n{4}".format(name, email, subject, message, phone))
        return JSONResponse({'msg': "Contact Request sent"}, status=200)