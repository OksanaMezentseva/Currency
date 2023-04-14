import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit

from currency.models import Rate
from currency.models import Source
from django_filters import CharFilter, filters
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
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Source
        fields = ['name']
