from dataclasses import dataclass

exchange_rates = {
    "base": "USD",
    "rates": {"USD": 1.00, "UAH": 40.00, "EUR": 0.9817, "GBP": 0.8495},
}


@dataclass
class Price:

    amount: int or float
    currency: str

    def __post_init__(self):
        self.currency = self.currency.upper()

    def __str__(self) -> str:
        return f"Total prise is - {self.amount} {self.currency}"

    def __add__(self, other: "Price") -> "Price":
        # not convertation
        if self.currency == other.currency:
            return Price(round(self.amount + other.amount, 2), self.currency)
        # regular convertation
        elif self.currency != other.currency and other.currency == "USD":
            return Price(
                round(
                    self.amount + other.amount * exchange_rates["rates"][self.currency],
                    2,
                ),
                self.currency,
            )
        # double convertion
        else:
            return Price(
                round(
                    self.amount
                    + (other.amount / exchange_rates["rates"][other.currency])
                    * exchange_rates["rates"][self.currency],
                    2,
                ),
                self.currency,
            )

    def __sub__(self, other: "Price") -> "Price":
        # not convertation
        if self.currency == other.currency:
            return Price(round(self.amount - other.amount, 2), self.currency)
        # regular convertation
        elif self.currency != other.currency and other.currency == "USD":
            return Price(
                round(
                    self.amount - other.amount * exchange_rates["rates"][self.currency],
                    2,
                ),
                self.currency,
            )
        # double convertion
        else:
            return Price(
                round(
                    self.amount
                    - (other.amount / exchange_rates["rates"][other.currency])
                    * exchange_rates["rates"][self.currency],
                    2,
                ),
                self.currency,
            )


def main():
    a = Price(1, "Eur")
    b = Price(40, "Usd")

    a_2 = Price(10, "usd")
    b_2 = Price(40, "UaH")

    total_price = a + b
    total_price_2 = a_2 - b_2
    print(total_price, "\n", total_price_2)


if __name__ == "__main__":
    main()
