from currency.services.base import BaseParserService


class MonoParserService(BaseParserService):

    def get_rates(self):

        import requests
        from currency.choices import RateCurrencyChoices
        from currency.utils import to_2_point_decimal, get_currency_code

        url = 'https://api.monobank.ua/bank/currency'
        available_currency = {
            'USD': RateCurrencyChoices.USD,
            'EUR': RateCurrencyChoices.EUR,
        }

        response = requests.get(url)
        response.raise_for_status()
        rates_raw = response.json()
        rates = []

        for rate in rates_raw:
            if get_currency_code(rate['currencyCodeB']) != 'UAH' \
                    or get_currency_code(rate['currencyCodeA']) not in available_currency:
                continue

            buy = to_2_point_decimal(rate['rateBuy'])
            sale = to_2_point_decimal(rate['rateSell'])
            currency = get_currency_code(rate['currencyCodeA'])

            rates.append({'buy': buy, 'sale': sale, 'currency': currency})

        return rates

    def get_source(self):
        data_source = {
            'name': 'MonoBank',
            'source_url': 'https://api.monobank.ua/bank/currency',
        }
        return data_source
