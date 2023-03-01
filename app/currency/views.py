from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.models import ContactUs
from currency.models import Rate, Source
from currency.forms import RateForm, SourceForm


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


def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)
    context = {
        'rate': rate
    }

    return render(request, 'rate_details.html', context)


def rates_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }

    return render(request, 'rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        # try:
        #     rate = Rate.objects.get(id=pk)
        # except Rate.DoesNotExist:
        #     raise Http404('Rate does not exist')
        form = RateForm(instance=rate)

    context = {
        'form': form
    }

    return render(request, 'rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        context = dict(rate=rate)

    return render(request, 'rates_delete.html', context)


def list_sources(request):
    sources = Source.objects.all()
    context = {
        'sources': sources
    }

    return render(request, 'sources_list.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)
    context = {
        'source': source
    }

    return render(request, 'source_details.html', context)


def sources_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form
    }

    return render(request, 'sources_create.html', context)


def sources_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form
    }

    return render(request, 'sources_update.html', context)


def sources_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        context = dict(source=source)

    return render(request, 'sources_delete.html', context)
