from currency.services.base import BaseParserService


class PrivatParserService(BaseParserService):

    def get_rates(self):

        import requests
        from currency.choices import RateCurrencyChoices
        from currency.utils import to_2_point_decimal

        url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
        available_currency = {
            'USD': RateCurrencyChoices.USD,
            'EUR': RateCurrencyChoices.EUR,
        }

        response = requests.get(url)
        response.raise_for_status()
        rates_raw = response.json()
        rates = []

        for rate in rates_raw:
            if rate['ccy'] not in available_currency:
                continue

            buy = to_2_point_decimal(rate['buy'])
            sale = to_2_point_decimal(rate['sale'])
            currency = rate['ccy']

            rates.append({'buy': buy, 'sale': sale, 'currency': currency})

        return rates

    def get_source(self):
        data_source = {
                'name': 'PrivatBank',
                'source_url': 'https://api.privatbank.ua/',
            }
        return data_source
