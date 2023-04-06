from celery import shared_task
import requests
from currency.choices import RateCurrencyChoices

from settings import settings

from currency.constants import PRIVATBANK_CODE_NAME
from currency.utils import to_2_point_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    source_pb, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME,
                                                defaults={
                                                    'name': 'PrivatBank',
                                                    'source_url': url
                                                })

    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = to_2_point_decimal(rate['buy'])
        sale = to_2_point_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source_pb,
        ).first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source_pb
            )


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
