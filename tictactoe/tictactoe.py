import sys

TICTAC = "_________"


def create_field(): # Function to create field
    print("▁▁▁▁▁▁▁")
    print(f"|{TICTAC[0]} {TICTAC[1]} {TICTAC[2]}|\n|{TICTAC[3]} {TICTAC[4]} {TICTAC[5]}|")
    print(f"|{TICTAC[6]} {TICTAC[7]} {TICTAC[8]}|")
    print("▔▔▔▔▔▔▔")


create_field()

fields_coords = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]  # Coordinations

combinations = ["012", "036", "048", "147", "258", "246", "345", "678"]  # Check if someone won

CURRENT_SYMBOL = 0 # Variable for present symbol - "X" or "O"


def user_input_coords(user_coordination):  # Function for users coordination
    splitted_str = user_coordination.split(' ')
    if (user_coordination[0]
        + user_coordination[2]).isdigit() != True:  # Checks if user inputed numbers and not text
        print("You should enter numbers!")
    elif int(splitted_str[0])\
            > 3 or int(splitted_str[1]) > 3:  # Checks if user inputed numbers in range from 1 to 3
        print("Coordinates should be from 1 to 3!")
    elif int(splitted_str[0])\
            < 1 or int(splitted_str[1]) < 1:  # Checks if user inputed numbers in range from 1 to 3
        print("Coordinates should be from 1 to 3!")
    return user_coordination


def user_moves():
    global TICTAC, CURRENT_SYMBOL
    for i in range(9):
        if user_coords == fields_coords[i]:
            if TICTAC[i] != "_": # Cchecks if field is occupied or not
                print("This cell is occupied! Choose another one!")
            else:
                changed_symbol = list(TICTAC) # transforms string to list to change symbol
                changed_symbol[i] = "X" # First move
                if CURRENT_SYMBOL == 0:
                    changed_symbol[i] = "X"
                    CURRENT_SYMBOL = 1
                else:
                    changed_symbol[i] = "O"
                    CURRENT_SYMBOL = 0
                TICTAC = ''.join(changed_symbol)
            create_field()
        else:
            continue


def game_status():
    global TICTAC
    for i in range(len(combinations)):
        combination = combinations[i] # Goes over combinations
        phrase = TICTAC[int(combination[0])]\
                 + TICTAC[int(combination[1])] + TICTAC[int(combination[2])] # Smth
        counter = 0 # Variable
        if phrase == "XXX":
            if counter == 1:
                print("Impossible")
            else:
                print("X win!")
            sys.exit()
        if phrase == "OOO":
            if counter == 1:
                print("Impossible")
            else:
                print("O win!")
            sys.exit()
        else:
            if (TICTAC.count("X") - TICTAC.count("O")) >= 2\
                    or (TICTAC.count("O") - TICTAC.count("X")) >= 2:
                print("Impossible")
                sys.exit()
            if "_" in TICTAC:
                continue
            else:
                print("Draw")
                sys.exit()
            continue
def game(user_coordinations):

    user_input_coords(user_coordinations)  # Users coordinations

    user_moves()

    game_status()

if __name__ == "__main__":
    while True:
        user_coords = input("Enter the coordinates:")
        if user_coords[0].isnumeric() or user_coords[2].isnumeric():
            game(user_coords)
        else:
            print("You inputed wrong coordinates")
