from rest_framework import serializers

from currency.models import Rate, Source, ContactUs
from settings import settings


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'address',
            'phone',
            'logo'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email_from',
            'subject',
            'message',
        )

    def create(self, validated_data):
        contact_us = ContactUs.objects.create(**validated_data)
        recipient = settings.DEFAULT_FROM_EMAIL  # noqa: F841
        from django.core.mail import send_mail
        send_mail(
            validated_data['subject'],
            validated_data['message'],
            validated_data['email_from'],
            ['recipient'],
            fail_silently=False,
        )
        return contact_us
