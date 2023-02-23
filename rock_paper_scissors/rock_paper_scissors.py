import random
import csv
import sys
import combinations

class Game:
    def __init__(self, userName):
        self.userOption = ""
        self.botOption = ""
        self.userName = userName
        self.scores = 0
        self.gameType = ""
        self.options = []

    def usualGame(self):
        """Usual game with rock, paper and scissors"""
        combos = combinations.combinationsUsual
        self.options = [key for key, _ in combos.items()]
        print(f"\nYour options: {', '.join(self.options)}")

        self.userOption = input("Input your option ")

        if self.userOption == "!exit":
            print("Bye!")
            sys.exit()
        if self.userOption not in self.options:
            print("Invalid value")
            return False

        self.botOption = random.choice(self.options)
        # print(self.botOption)
        # self.userOption = userChoice

        if self.userOption.__eq__(self.botOption):
            self.addScore(50)
            print(f"There is a draw ({self.botOption})")
        if self.botOption in combos[self.userOption]:
            self.addScore(100)
            print(f"Well done. The computer chose {self.botOption} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.botOption}")

    def extendedGame(self):
        """Extended game with rock, scissors, paper, fire, snake,
         human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun"""
        combos = combinations.combinationsExtended
        self.options = [key for key, _ in combos.items()]

        print(f"Your options: {', '.join(self.options)}")

        self.userOption = input("Input your option ")

        if self.userOption == "!exit":
            print("Bye!")
            sys.exit()
        if self.userOption not in self.options:
            print("Invalid value")
            return False

        self.botOption = random.choice(self.options)

        if self.userOption.__eq__(self.botOption):
            self.addScore(50)
            print(f"There is a draw ({self.botOption})")
        if self.botOption in combos[self.userOption]:
            self.addScore(100)
            print(f"Well done. The computer chose {self.botOption} and failed ")
            # break
        else:
            print(f"Sorry, but the computer chose {self.botOption}")

    def checkUser(self):
        """Check if user is already existing or not"""
        with open("rating.csv", 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line.__contains__(self.userName):
                    self.scores = int(line[1])
                    return int(line[1])

        with open("rating.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([self.userName, 0])
            self.scores = 0
            return 0

    def addScore(self, score):
        """Adds score to user"""
        with open('rating.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open('rating.csv', mode='w+', newline='\n') as file:
            writer = csv.writer(file)
            for i, row in enumerate(rows):
                if len(row) > 0 and row[0].__contains__(self.userName):
                    rows[i][1] = int(rows[i][1]) + score

            writer.writerows(rows)

    def printMenu(self):
        """Printing menu of game"""
        print("Select option:")
        print("Type 1 for Usual game")
        print("Type 2 for Extended version")
        print("Type 3 to see your stats")
        self.userType = input('>')

        self.chooseType()

    def chooseType(self):
        """Choosing type of game"""
        match self.userType:
            case '1':
                print("Okay, let`s start.")
                self.gameType = "Usual"
            case '2':
                print("Okay, let`s start.")
                self.gameType = "Extended"
            case '3':
                print("Here your stats")
                print(f"Username:{self.userName}|Scores:{self.scores}")
                self.printMenu()
            case _:
                print("Oh no! Incorrect type!\nTry again!!!")

    def chooseGame(self):
        """Choosegame"""
        if self.gameType == "Usual":
            self.usualGame()
        if self.gameType == "Extended":
            self.extendedGame()


if __name__ == "__main__":
    userName = input("Enter your name:")
    new = Game(userName)
    new.checkUser()
    print(f"Hello, {userName}!")
    new.printMenu()
    while True:
        new.chooseGame()

#DeFakto
