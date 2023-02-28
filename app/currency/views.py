from django.shortcuts import render

from currency.models import ContactUs
from currency.models import Rate


def contact_list(request):
    contacts = ContactUs.objects.all()
    context = {
        'contacts': contacts
    }

    return render(request, 'contact_list.html', context)


def list_rates(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)
