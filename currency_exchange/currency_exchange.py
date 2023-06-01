import requests
import json

URL = "http://www.floatrates.com/daily/{value}.json"
cache = dict()


class Exchange:

    @staticmethod
    def request_to_webpage(currency: str) -> str | None:
        """
            Requesting webpage using requested currency
            currency: str - Currency that user wants to see
            return: str or None
        """
        try:
            response = requests.get(URL.format(value=currency.lower()))
            response_data = json.loads(response.text)
            return response_data
        except json.decoder.JSONDecodeError:
            print("Incorrect currency!")
            return

    @staticmethod
    def currency_request(quantity: float, user_currency: str, requested_currency: str) -> None:
        """
            Managing and checking user input values
            parameters:
            quantity: float - Quantity of money
            user_currency: str - Currency that user own
            requested_currency: str - Currency that user requesting
            return: None
        """
        if user_currency not in cache:
            cache[user_currency] = Exchange.request_to_webpage(user_currency)

        try:
            response_data = cache[user_currency]
            requested_currency_value = response_data[requested_currency]["rate"]
            print(f"{quantity} {user_currency.upper()} in USD is {requested_currency_value * quantity}")
        except (TypeError, KeyError):
            raise ValueError("Invalid currency")


if __name__ == "__main__":
    value_is_correct: bool = False
    user_currency: str = ""
    while not value_is_correct:
        user_currency = input("Input your currency > ")
        if Exchange.request_to_webpage(user_currency) is not None:
            value_is_correct = True

    value_is_correct = False
    quantity: float = 0
    while True:
        while not value_is_correct:
            try:
                quantity = float(input("Input quantity of your currency> "))
                value_is_correct = True
            except ValueError:
                print("Incorrect quantity")
                value_is_correct = False
                break

            value_is_correct = False

            requested_currency = input("Input currency that you need > ")
            Exchange.currency_request(quantity, user_currency, requested_currency)

