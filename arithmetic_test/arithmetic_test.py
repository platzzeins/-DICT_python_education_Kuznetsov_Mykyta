"""Importing system, time modules and tests.py file"""
import sys, tests


def get_data(result, level):
    """get data of user"""
    name = input("What is your name?")
    return f"{name}: {result}/5 in Level {level}"


def main(argument):
    """User choice for type of game"""
    results = 0
    if argument > 5 or argument <= 0:
        print("Incorrect format.")
    match argument:
        case 1:
            for _ in range(0, 5):
                results += tests.first_type()
        case 2:
            for _ in range(0, 5):
                results += tests.second_type()
        case 3:
            for _ in range(0, 5):
                results += tests.third_type()
        case 4:
            for _ in range(0, 5):
                results += tests.fourth_type()
        case 5:
            for _ in range(0, 5):
                results += tests.determinant()
    print(f"Your mark is {results}/5!")
    write_or_not = input("Would you like to save the result? Enter yes or no.")
    if write_or_not in ("yes", "y", "Y", "Yes", "YES"):
        with open("results.txt", "w", encoding="utf-8") as file:
            info = get_data(results, argument)
            file.write(info)
            file.close()
    sys.exit()


if __name__ == "__main__":
    while True:
        USER_CHOOSE = 0
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - find unknown number
4 - find area of figure
5 - find determinant of matrix""")
        try:
            USER_CHOOSE = int(input())
        except ValueError:
            print("Incorrect format.")
        finally:
            main(USER_CHOOSE)


#DeFakto
