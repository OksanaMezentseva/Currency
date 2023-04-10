from celery import shared_task

from settings import settings

from currency.services.privat_parser import PrivatParserService
from currency.services.mono_parser import MonoParserService


@shared_task
def parse_monobank():
    from currency.constants import MONOBANK_CODE_NAME

    parser = MonoParserService()
    rates = parser.get_rates()
    source = parser.get_source()
    parser.save_rates(rates, MONOBANK_CODE_NAME, source)


@shared_task
def parse_privatbank():
    from currency.constants import PRIVATBANK_CODE_NAME

    parser = PrivatParserService()
    rates = parser.get_rates()
    source = parser.get_source()
    parser.save_rates(rates, PRIVATBANK_CODE_NAME, source)


@shared_task(autoretry_for=(ConnectionError,),
             retry_kwargs={'max_retries': 5})
def send_mail(subject, message):
    raise ConnectionError
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
