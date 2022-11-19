from dataclasses import dataclass

exchange_rates = {
    "base": "USD",
    "rates": {"USD": 1.00, "UAH": 40.00, "EUR": 0.9817, "GBP": 0.8495},
}

# uah, eur:
# uah + (eur -> usd -> uah)
# eur, uah:
# eur + (uah -> usd -> eur)
# uah, usd:
# uah + (usd -> uah)
# usd, uah:
# usd + (uah -> usd)
# eur, eur:
# eur + eur


@dataclass
class DataPrice:
    amount: int or float
    currency: str

    def __post_init__(self):
        self.currency = self.currency.upper()

    def __str__(self) -> str:
        return f"Total prise is - {self.amount} {self.currency}"


class Price:
    def __init__(self, dataprice: "DataPrice") -> None:
        self.price = dataprice

    def __add__(self, other: "DataPrice") -> "DataPrice":
        # not convertation
        if self.price.currency == other.price.currency:
            return DataPrice(
                round(self.price.amount + other.price.amount, 2), self.price.currency
            )
        # regular convertation
        elif (
            self.price.currency != other.price.currency
            and other.price.currency == "USD"
        ):
            return DataPrice(
                round(
                    self.price.amount
                    + other.price.amount * exchange_rates["rates"][self.price.currency],
                    2,
                ),
                self.price.currency,
            )
        # double convertion
        else:
            return DataPrice(
                round(
                    self.price.amount
                    + (
                        other.price.amount
                        / exchange_rates["rates"][other.price.currency]
                    )
                    * exchange_rates["rates"][self.price.currency],
                    2,
                ),
                self.price.currency,
            )

    def __sub__(self, other: "DataPrice") -> "DataPrice":
        # not convertation
        if self.price.currency == other.price.currency:
            return DataPrice(
                round(self.price.amount - other.price.amount, 2), self.price.currency
            )
        # regular convertation
        elif (
            self.price.currency != other.price.currency
            and other.price.currency == "USD"
        ):
            return DataPrice(
                round(
                    self.price.amount
                    - other.price.amount * exchange_rates["rates"][self.price.currency],
                    2,
                ),
                self.price.currency,
            )
        # double convertion
        else:
            return DataPrice(
                round(
                    self.price.amount
                    - (
                        other.price.amount
                        / exchange_rates["rates"][other.price.currency]
                    )
                    * exchange_rates["rates"][self.price.currency],
                    2,
                ),
                self.price.currency,
            )


def main():
    a = DataPrice(1, "Eur")
    b = DataPrice(40, "Usd")

    a_2 = DataPrice(10, "usd")
    b_2 = DataPrice(40, "UaH")

    total_price = Price(a) + Price(b)
    total_price_2 = Price(a_2) - Price(b_2)
    print(total_price, "\n", total_price_2)


if __name__ == "__main__":
    main()
