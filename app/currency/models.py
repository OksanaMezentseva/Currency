from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=55)
    subject = models.CharField(max_length=55)
    message = models.TextField()


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=25)  # usd, eur
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)


class Source(models.Model):
    name = models.CharField(max_length=65)
    source_url = models.URLField(max_length=255)
    address = models.CharField(max_length=65, null=True)
    phone = models.CharField(max_length=65, null=True)
    created = models.DateTimeField(auto_now_add=True)
