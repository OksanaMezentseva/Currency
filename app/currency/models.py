from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=55)
    subject = models.CharField(max_length=55)
    message = models.TextField()

