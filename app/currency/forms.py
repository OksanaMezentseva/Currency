from django import forms

from currency.models import Rate
from currency.models import Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'source',
            'currency'
        )


class SourceForm(forms.ModelForm):
    address = forms.CharField(required=False)
    phone = forms.CharField(required=False)

    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'address',
            'phone'
        )
