import re


class RegularExpressions:
    def __init__(self):
        self.regex = ""

    def parse_input(self, user_input) -> str | None:
        """
            Parsing user input phrase
            user_input: str = user input phrase
            return: str | None
        """
        try:
            self.regex, string = user_input.split("|")
            return string.strip()
        except ValueError:
            print("Invalid input!")
            return None

    def check_match(self, string) -> bool:
        """
            Checking if there is regular expression matches
            string: str - user phrase
            return: bool
        """
        return re.search(self.regex, string) is not None

    def loop(self):
        """
            Main program loop
            return: None
        """
        while True:
            user_input = input("Enter your expression: ")
            string = self.parse_input(user_input)
            if string is None:
                continue
            if self.check_match(string):
                print("True")
            else:
                print("False")


def main():
    """
        Start point of program
        return: None
    """
    regex = RegularExpressions()
    regex.loop()


if __name__ == "__main__":
    main()
