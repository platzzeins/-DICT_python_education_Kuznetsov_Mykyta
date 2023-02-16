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
            print(f"Bot chose {self.botOption}")
            print("Draw")
        for i, j in combinations.items():
            if self.userOption == i and self.botOption == j:
                print(f"Bot chose {self.botOption}")
                print("First player won!")
                break
            elif self.botOption == i and self.userOption == j:
                print(f"Bot chose {self.botOption}")
                print("Second player won!")
                break


if __name__ == "__main__":
    while True:
        userChoice = input("Input your option ")
        new = game(userChoice)
        new.actual_game()
