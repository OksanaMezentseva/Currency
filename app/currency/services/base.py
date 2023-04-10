class BaseParserService:
    def get_rates(self) -> dict:
        # method to get currency rates from source
        raise NotImplementedError

    def get_source(self) -> dict:
        # method to get source
        raise NotImplementedError

    def save_rates(self, rates, code_name, data_source):
        # method to save currency rates into DB
        from currency.models import Rate, Source
        from currency.choices import RateCurrencyChoices

        available_currency = {
            'USD': RateCurrencyChoices.USD,
            'EUR': RateCurrencyChoices.EUR,
        }

        source, created = Source.objects.get_or_create(
            code_name=code_name,
            defaults=data_source
        )

        for rate in rates:
            if rate['currency'] not in available_currency:
                continue

            buy = rate['buy']
            sale = rate['sale']
            currency = rate['currency']

            last_rate = Rate.objects.filter(
                currency=available_currency[currency],
                source=source,
            ).first()

            if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
                Rate.objects.create(
                    buy=buy,
                    sale=sale,
                    currency=available_currency[currency],
                    source=source,
                )
