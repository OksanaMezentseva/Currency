import django_filters

from currency.models import Rate, ContactUs, Source
from django_filters import filters
from currency.choices import RateCurrencyChoices


class RateFilter(django_filters.FilterSet):
    currency = django_filters.ChoiceFilter(choices=RateCurrencyChoices.choices)
    source = filters.ModelChoiceFilter(queryset=Source.objects.all())
    buy = django_filters.NumberFilter(field_name='buy', lookup_expr='exact')
    sale = django_filters.NumberFilter(field_name='sale', lookup_expr='exact')

    class Meta:
        model = Rate
        fields = []


class SourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Source
        fields = ['name']


class ContactUsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email_from = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.CharFilter(lookup_expr='icontains')
    message = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ContactUs
        fields = ['name',
                  'email_from',
                  'subject',
                  'message']
