from django.http import HttpResponse

from currency.models import ContactUs
from currency.models import Rate


def contact_list(request):
    contacts = ContactUs.objects.all()
    result = []

    for contact in contacts:
        result.append(
            f'id: {contact.id}, email_from: {contact.email_from}, subject: {contact.subject},'
            f' message: {contact.message} <br>')
    return HttpResponse(str(result))


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(
            f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell},'
            f' source: {rate.source}, created: {rate.created}, currency: {rate.currency} <br>')
    return HttpResponse(str(result))
