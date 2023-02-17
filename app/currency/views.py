from django.shortcuts import render
from django.http import HttpResponse

from currency.models import ContactUs


def contact_list(request):
    contacts = ContactUs.objects.all()
    result = []

    for contact in contacts:
        result.append(
            f'id: {contact.id}, email_from: {contact.email_from}, subject: {contact.subject}, message: {contact.message} <br>')
    return HttpResponse(str(result))
