combinations_win = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
combinations_fall = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


class game():
    def __init__(self, userChoice):
        self.userOption = userChoice
        self.botOption = ""

    def win_bot(self):
        self.botOption = combinations_fall[self.userOption]
        print(self.userOption)
        print(f"Sorry, but the computer chose {self.botOption}")


if __name__ == "__main__":
    while True:
        userChoice = input("Input your option ")
        new = game(userChoice)
        new.win_bot()
