from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank


def test_privatbank_parser(mocker):
    initial_count = Rate.objects.all().count()
    privat_data = [{"ccy": "EUR", "base_ccy": "UAH", "buy": "40.06640", "sale": "41.84100"},
                   {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: privat_data
        )
    )

    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 1

    # parse_privatbank()
    # assert Rate.objects.all().count() == initial_count + 2
    #
    # assert request_get_mock.call_count == 2
