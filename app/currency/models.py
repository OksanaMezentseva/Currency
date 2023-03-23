from django.db import models

from currency.choices import RateCurrencyChoices


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=55)
    subject = models.CharField(max_length=55)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )  # if field has choices - get_{field_name}_display(), get_currency_display()
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    # source = models.CharField(max_length=25)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class Source(models.Model):
    name = models.CharField(max_length=65)
    source_url = models.URLField(max_length=255)
    address = models.CharField(max_length=65, null=True)
    phone = models.CharField(max_length=65, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=511)
    request_method = models.CharField(max_length=10)
    time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
