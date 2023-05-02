from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank, parse_monobank


def test_privatbank_parser(mocker):
    initial_count = Rate.objects.all().count()
    privat_data = [{"ccy": "EUR", "base_ccy": "UAH", "buy": "45.06640", "sale": "40.84100"},
                   {"ccy": "USD", "base_ccy": "UAH", "buy": "46.56860", "sale": "30.45318"}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: privat_data
        )
    )

    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2

    assert request_get_mock.call_count == 2


def test_monobank_parser(mocker):
    initial_count = Rate.objects.all().count()
    mono_data = [
        {
            'currencyCodeA': '978',
            'currencyCodeB': '980',
            'rateBuy': '40.06640',
            'rateSell': '45.84100',
        },
        {
            'currencyCodeA': '840',
            'currencyCodeB': '980',
            'rateBuy': '31.56860',
            'rateSell': '35.45318',
        }
    ]

    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: mono_data
        )
    )

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    assert request_get_mock.call_count == 2
