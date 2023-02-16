import random

combinations = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
options = ["rock", "paper", "scissors"]


class game():
    def __init__(self, userChoice):
        self.userOption = userChoice
        self.botOption = ""

    def actual_game(self):
        self.botOption = random.choice(options)

        if self.userOption.__eq__(self.botOption):
            print(f"There is a draw ({self.botOption})")
        for i, j in combinations.items():
            if self.userOption == i and self.botOption == j:
                print(f"Well done. The computer chose {self.botOption} and failed ")
                break
            elif self.botOption == i and self.userOption == j:
                print(f"Sorry, but the computer chose {self.botOption}")
                break


if __name__ == "__main__":
    while True:
        userChoice = input("Input your option ")
        if userChoice in options:
            new = game(userChoice)
            new.actual_game()
        elif userChoice == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input")

