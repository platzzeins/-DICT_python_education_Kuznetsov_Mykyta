"""Importing random, sys modules and file file_manipulator as module"""
import random
import sys
import file_manipulator


class Game:
    """Class Game for game Rock, Paper, Scissors(classic, extended and custom versions)"""
    def __init__(self, user_name: str):
        self.user_option = ""
        self.bot_option = ""
        self.user_name = user_name
        self.scores = 0
        self.game_type = ""
        self.options = []
        self.custom_elements = []
        self.game_list = []
        self.user_type = ""

    def usual_game(self):
        """
            Usual game with rock, paper and scissors
            return: None
        """
        local_game_list = ["paper", "rock", "scissors"]

        self.user_option = input("Input your option ")

        if self.user_option == "!exit":
            print("Bye!")
            sys.exit()
        if self.user_option not in local_game_list:
            print("Invalid value")
            return False

        self.bot_option = random.choice(local_game_list)

        arch = self.combos(local_game_list)

        if self.user_option == self.bot_option:
            self.add_score(50)
            print(f"There is a draw ({self.bot_option})")
        elif self.bot_option in arch:
            self.add_score(100)
            print(f"Well done. The computer chose {self.bot_option} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.bot_option}")

    def start_extended_game(self):
        """
            Extended game with rock, scissors, paper, fire, snake,
            human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun
            return: None
        """

        local_game_list = ["paper", "air", "water", "dragon", "devil", "lightning", "gun", "rock",
                         "fire", "scissors", "snake", "human", "tree", "wolf", "sponge"]

        self.user_option = input("Input your option ")

        if self.user_option == "!exit":
            print("Bye!")
            sys.exit()
        if self.user_option not in local_game_list:
            print("Invalid value")
            return False

        self.bot_option = random.choice(self.game_list)

        arch = self.combos(local_game_list)

        if self.user_option == self.bot_option:
            self.add_score(50)
            print(f"There is a draw ({self.bot_option})")
        elif self.bot_option in arch:
            self.add_score(100)
            print(f"Well done. The computer chose {self.bot_option} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.bot_option}")

    def combos(self, local_game_list):
        """
            Winning combinations creation
            local_game_list = List with all entity's for chosen game, type -- list
            return: None
        """
        add_arch = []
        position = local_game_list.index(self.user_option)
        if len(local_game_list[local_game_list.index(self.user_option): -1]) \
                < round(len(local_game_list) / 2):
            add_arch = local_game_list[0: len(local_game_list
                                              ) - position - round(len(local_game_list) / 2)]
            print(add_arch)

        arch = local_game_list[position + 1: position + round(len(local_game_list) / 2)] + add_arch
        return arch

    def create_game(self):
        """
            Input custom game from user
            return: None
        """
        print("Input your elements separated with comas like: \n rock,paper,scissors")
        elements_input = input()
        self.custom_elements = elements_input.split(',')

    def start_custom_game(self):
        """Custom game with user elements"""
        local_game_list = self.custom_elements

        print(f"Your options: {local_game_list}")

        self.user_option = input("Input your option ")

        if self.user_option == "!exit":
            print("Bye!")
            sys.exit()
        if self.user_option not in local_game_list:
            print("Invalid value")
            return False

        self.bot_option = random.choice(self.custom_elements)

        arch = self.combos(local_game_list)

        if self.user_option == self.bot_option:
            self.add_score(50)
            print(f"There is a draw ({self.bot_option})")
        elif self.bot_option in arch:
            self.add_score(100)
            print(f"Well done. The computer chose {self.bot_option} and failed ")
        else:
            print(f"Sorry, but the computer chose {self.bot_option}")

    def check_user(self):
        """
            Check if user is already existing or not
            return: None
        """
        self.scores = file_manipulator.check_user(self.user_name)

    def add_score(self, score):
        """
            Adds score to user
            return: None
        """
        file_manipulator.add_score(score, self.user_name)

    def print_menu(self):
        """
            Printing menu of game
            return: None
        """
        print("Select option:")
        print("Type 1 for Usual game")
        print("Type 2 for Extended version")
        print("Type 3 for custom game")
        print("Type 4 to see your stats")

        self.user_type = input('>')

        self.choose_type()

    def choose_type(self):
        """
            Choosing type of game
            return: None
        """
        match self.user_type:
            case '1':
                print("Okay, let`s start.")
                self.game_type = "Usual"
            case '2':
                print("Okay, let`s start.")
                self.game_type = "Extended"
            case '3':
                print("Okay, let`s start.")
                self.game_type = "Custom"
                self.create_game()
            case '4':
                print("Here your stats")
                print(f"user_name:{self.user_name}|Scores:{self.scores}")
                self.print_menu()
            case _:
                print("Oh no! Incorrect type!\nTry again!!!")

    def choose_game(self):
        """
            Choose game
            return: None
        """
        if self.game_type == "Usual":
            self.usual_game()
        if self.game_type == "Extended":
            self.start_extended_game()
        if self.game_type == "Custom":
            self.start_custom_game()


if __name__ == "__main__":
    input_user_name = input("Enter your name:")
    new = Game(input_user_name)
    new.check_user()
    print(f"Hello, {input_user_name}!")
    new.print_menu()
    while True:
        new.choose_game()


#DeFakto

