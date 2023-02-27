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
