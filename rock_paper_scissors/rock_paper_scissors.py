import random
import sys
import fileManipulator


class Game:
    def __init__(self, userName):
        self.userOption = ""
        self.botOption = ""
        self.userName = userName
        self.scores = 0
        self.gameType = ""
        self.options = []
        self.customElements = []
        self.gameList = ["paper", "air", "water", "dragon", "devil", "lightning", "gun", "rock",
                         "fire", "scissors", "snake", "human", "tree", "wolf", "sponge"]

    def usualGame(self):
        """Usual game with rock, paper and scissors"""
        localGameList = ["paper", "rock", "scissors"]

        self.userOption = input("Input your option ")

        if self.userOption == "!exit":
            print("Bye!")
            sys.exit()
        if self.userOption not in localGameList:
            print("Invalid value")
            return False

        self.botOption = random.choice(localGameList)

        arch = self.combos(localGameList)

        if self.userOption == self.botOption:
            self.addScore(50)
            print(f"There is a draw ({self.botOption})")
        elif self.botOption in arch:
            self.addScore(100)
            print(f"Well done. The computer chose {self.botOption} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.botOption}")


    def extendedGame(self):
        """Extended game with rock, scissors, paper, fire, snake,
         human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun"""

        localGameList = ["paper", "air", "water", "dragon", "devil", "lightning", "gun", "rock",
                         "fire", "scissors", "snake", "human", "tree", "wolf", "sponge"]

        self.userOption = input("Input your option ")

        if self.userOption == "!exit":
            print("Bye!")
            sys.exit()
        if self.userOption not in localGameList:
            print("Invalid value")
            return False

        self.botOption = random.choice(self.gameList)

        arch = self.combos(localGameList)

        if self.userOption == self.botOption:
            self.addScore(50)
            print(f"There is a draw ({self.botOption})")
        elif self.botOption in arch:
            self.addScore(100)
            print(f"Well done. The computer chose {self.botOption} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.botOption}")

    def combos(self, localGameList):
        add_arch = []
        position = localGameList.index(self.userOption)
        if len(localGameList[localGameList.index(self.userOption): -1]) < round(len(localGameList) / 2):
            add_arch = localGameList[0: len(localGameList) - position - round(len(localGameList) / 2)]
            print(add_arch)

        arch = localGameList[position + 1: position + round(len(localGameList) / 2)] + add_arch
        return arch

    def createGame(self):
        print("Input your elements separated with comas like: \n rock,paper,scissors")
        elementsInput = input()
        self.customElements = elementsInput.split(',')

    def customGame(self):
        localGameList = self.customElements


        print(f"Your options: {localGameList}")

        self.userOption = input("Input your option ")

        if self.userOption == "!exit":
            print("Bye!")
            sys.exit()
        if self.userOption not in localGameList:
            print("Invalid value")
            return False

        self.botOption = random.choice(self.customElements)

        arch = self.combos(localGameList)

        if self.userOption == self.botOption:
            self.addScore(50)
            print(f"There is a draw ({self.botOption})")
        elif self.botOption in arch:
            self.addScore(100)
            print(f"Well done. The computer chose {self.botOption} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.botOption}")



    def checkUser(self):
        """Check if user is already existing or not"""
        self.scores = fileManipulator.checkUser(self.userName)

    def addScore(self, score):
        """Adds score to user"""
        fileManipulator.addScore(score, self.userName)

    def printMenu(self):
        """Printing menu of game"""
        print("Select option:")
        print("Type 1 for Usual game")
        print("Type 2 for Extended version")
        print("Type 3 for custom game")
        print("Type 4 to see your stats")

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
                print("Okay, let`s start.")
                self.gameType = "Custom"
                self.createGame()
            case '4':
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
        if self.gameType == "Custom":
            self.customGame()


if __name__ == "__main__":
    userName = input("Enter your name:")
    new = Game(userName)
    new.checkUser()
    print(f"Hello, {userName}!")
    new.printMenu()
    while True:
        new.chooseGame()

#DeFakto
