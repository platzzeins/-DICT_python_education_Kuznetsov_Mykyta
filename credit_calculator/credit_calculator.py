"""Module for calculating credit payments"""
import math
from argparse import ArgumentParser


class Calculator:
    """Calculator class"""
    def __init__(self):
        self.parser = ArgumentParser(description="Credit calculator")
        self.parser.add_argument("--type", required=True,
                                 choices=["annuity", "diff"], help="Type of payment")
        self.parser.add_argument("--principal", type=float, help="Credit principal")
        self.parser.add_argument("--periods", type=int, help="Number of payments")
        self.parser.add_argument("--interest", type=float, help="Interest rate")
        self.parser.add_argument("--payment", type=float, help="N=Month payment")
        args = self.parser.parse_args()
        self.principal = args.principal
        self.type = args.type
        self.month_payment = args.payment
        self.number_of_months = args.periods
        self.loan_interest = args.interest
        self.annuity_payment = 0

    @staticmethod
    def calculate_diff(loan_interest, number_of_months, principal):
        """Calculate differentiated payment
        loan_interest -- Loan interest = float
        number_of_months -- Number of months, type = int
        principal -- Principal, type = float
        """
        loan_interest = loan_interest / 100 / 12
        total_payments = 0
        for month in range(1, number_of_months + 1):
            diff = math.ceil(principal
                             / number_of_months + loan_interest
                             * (principal - (principal * (month - 1)) / number_of_months))
            total_payments += diff
            print(f"Month {month}: payment is {diff}")
        print(f"\nOverpayment = {total_payments - principal}")

    @staticmethod
    def calculate_annuity_payment(number_of_months, principal, loan_interest):
        """Calculate annuity payment
        number_of_months -- Number of months, type = int
        principal -- Principal, type = float
        loan_interest -- Loan interest = float
        """
        loan_interest = loan_interest / 100 / 12
        payment = principal * (loan_interest * pow(1 + loan_interest, number_of_months)
                               ) / (pow(1 + loan_interest, number_of_months) - 1)
        print(f"Your annuity payment = {payment}")
        print(f"Overpayment: {math.ceil(payment * number_of_months - principal)}")

    @staticmethod
    def calculate_annuity_number_of_months(principal, month_payment, loan_interest):
        """Calculate number of months
        principal -- Principal, type = float
        month_payment -- Month payment, type = float
        loan_interest -- Loan interest = float
        """
        loan_interest = (loan_interest / 100) / (12 * 1)
        number_of_months = math.ceil(math.log(
            (month_payment / (month_payment - loan_interest * principal)), 1 + loan_interest))
        if number_of_months % 12 != 0:
            print(f"It will take {int(number_of_months / 12)} years "
                  f"and {number_of_months % 12 } months to repay this loan!")
        else:
            print(f"It will take {int(number_of_months / 12)} years")

    @staticmethod
    def calculate_annuity_principal(number_of_months, month_payment, loan_interest):
        """Calculate principal
        number_of_months -- Number of months, type = int
        month_payment -- Month payment, type = float
        loan_interest -- Loan interest = float
        """
        i = loan_interest / 100 / 12
        principal = month_payment / ((i * pow(1 + i, number_of_months))
                                     / (pow(1 + i, number_of_months) - 1))
        print(f"Your loan principal = {int(principal)}!")
        print(f"Overpayment: {math.ceil(number_of_months * month_payment - principal)}")

    def check_diff(self):
        """Check if there is no errors for diff type"""
        if self.month_payment:
            self.parser.error(
                "Incorrect parameters: --payment can not be with diff type")
        if not self.number_of_months:
            self.parser.error(
                "Incorrect parameters: --periods is required with diff type")
        if not self.principal:
            self.parser.error(
                "Incorrect parameters: --principal is required with diff type")
        self.calculate_diff(self.loan_interest, self.number_of_months, self.principal)

    def check_annuity(self):
        """Check if there is no errors for annuity type"""
        if self.month_payment and self.number_of_months:
            self.calculate_annuity_principal(
                self.number_of_months, self.month_payment, self.loan_interest)
        elif self.principal and self.number_of_months:
            self.calculate_annuity_payment(
                self.number_of_months, self.principal, self.loan_interest)
        elif self.principal and self.month_payment:
            self.calculate_annuity_number_of_months(
                self.principal, self.month_payment, self.loan_interest)
        else:
            self.parser.error(
                "Incorrect parameters: --payment, --principal \
                and --periods are required with --type=annuity")

    def start(self):
        """Start function"""
        match self.type:
            case "diff":
                self.check_diff()
            case "annuity":
                self.check_annuity()


if __name__ == "__main__":
    calc = Calculator()
    calc.start()
