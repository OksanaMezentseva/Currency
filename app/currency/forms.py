from django import forms

from currency.models import Rate
from currency.models import Source
from currency.models import ContactUs

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'source',
            'currency'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            'name',
            'source_url',
            'address',
            'phone'
        )


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email_from',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-12'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email_from', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'subject',
            'message'
        )
