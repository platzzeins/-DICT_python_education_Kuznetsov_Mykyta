"""Importing random module"""
import random


def check_matrix(matrix1, matrix2):
    """Checks if all values in matrix are numbers"""
    if matrix2 == 0:
        for _, m1val in enumerate(matrix1):
            for k in range(len(m1val)):
                if not m1val[k].isnumeric():
                    return False
        return True

    else:
        for _, m1val in enumerate(matrix1):
            for k in range(len(m1val)):
                if not m1val[k].isnumeric():
                    return False
        for _, m2val in enumerate(matrix2):
            for k in range(len(m2val)):
                if not m2val[k].isnumeric():
                    return False
        return True


def make_nums(argument):
    """Making two or one random integers"""
    if argument == "one numb":
        return random.randrange(11, 29)
    return random.randrange(2, 9), random.randrange(2, 9)


def multiplying(numb_1, numb_2):
    """Multiplying test"""
    print(f"{numb_1} * {numb_2}")
    user_answer = 0
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
        raise
    finally:
        if (numb_1 * numb_2) == user_answer:
            print("Right!")
            return 1
        print("Wrong")
        return 0


def adding(numb_1, numb_2):
    """Adding test"""
    print(f"{numb_1} + {numb_2}")
    user_answer = 0
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
        raise
    finally:
        if (numb_1 + numb_2) == user_answer:
            print("Right!")
            return 1
        print("Wrong")
        return 0

def minus(numb_1, numb_2):
    """Minus test"""
    print(f"{numb_1} - {numb_2}")
    user_answer = 0
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
        minus(numb_1, numb_2)
    finally:
        if (numb_1 - numb_2) == user_answer:
            print("Right!")
            return 1
        print("Wrong")
        return 0


def first_type():
    """First type of questions"""
    numb_1, numb_2 = make_nums("two nums")


    choice = random.randrange(1, 3)
    match choice:
        case 1:
            return multiplying(numb_1, numb_2)
        case 2:
            return adding(numb_1, numb_2)
        case 3:
            return minus(numb_1, numb_2)


def second_type():
    """Second type of questions"""
    numb = make_nums("one numb")
    print(numb)
    user_answer = 0
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == (numb**2):
            print("Right!")
            return 1
        print("Wrong")
        return 0


def third_type():
    """Third type of questions"""
    numb_1, numb_2 = make_nums("two nums")
    to_find = random.randrange(1, 12)
    phrase = (numb_1 * to_find) + numb_2
    user_answer = 0
    print(f"{numb_1} * x + {numb_2} = {phrase}")
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == to_find:
            print("Right!")
            return 1
        print("Wrong")
        return 0


def circle():
    """Circle test"""
    radius = random.randrange(3, 10)
    print(f"Find the area of the circle, if radius = {radius} (type only integer before pi)")
    user_answer = 0
    try:
        user_answer = int(input("> "))
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == radius**2:
            print("Right!")
            return 1
        print("Wrong")
        return 0

def rectangle():
    """Rectangle test"""
    numb_1, numb_2 = make_nums("two nums")
    print(f"Find the area of rectangle, if a = {numb_1} and b = {numb_2}")
    user_answer = 0
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == (numb_1 * numb_2):
            print("Right!")
            return 1
        print("Wrong")
        return 0


def triangle():
    """Triangle test"""
    numb_1, numb_2 = make_nums("two nums")
    numb_3 = random.randrange(max(numb_1,numb_2), 13)
    print(f"Find the area of the right triangle, if a = {numb_1}, b = {numb_2} and c = {numb_3}")
    user_answer = 0
    try:
        user_answer = float(input("> "))
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == 0.5 * (numb_1 * numb_2):
            print("Right!")
            return 1
        print("Wrong")
        return 0


def fourth_type():
    """Fourth type of questions"""

    choice = random.randrange(1, 4)
    match choice:
        case 1:
            return circle()
        case 2:
            return rectangle()
        case 3:
            return triangle()


def determinant():
    """Fifth type of questions"""
    def minor(matrix, i, j):
        """Finding minor of matrix"""
        tmp = [row for k, row in enumerate(matrix) if k != i]
        # print(f" tmp 1 is {tmp}")
        tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
        # print(f" tmp 2 is {tmp}")
        return tmp


    def determinant_count(matrix):
        """Determinant counting"""

        if not check_matrix(matrix, 0):
            print("Enter only numbers")
            return False

        def det2(matrix):
            return int(matrix[0][0]) * int(matrix[1][1]) - int(matrix[0][1]) * int(matrix[1][0])

        def determinant(matrix):
            """ACtually finding determinant"""
            size = len(matrix)
            if size == 2:
                return det2(matrix)

            return sum((-1) ** j * int(matrix[0][j]) *
                       determinant(minor(matrix, 0, j)) for j in range(size))

        return determinant(matrix)


    def print_matrix(matrix):
        """Print matrix the way to comfortable see it"""
        for _, val in enumerate(matrix):
            for k in range(len(val)):
                print(val[k], end=' ')
            print()


    matrix = [[],[],[]]
    for _ in range(0, 3):
        for j in range(len(matrix)):
            matrix[j].append(random.randrange(1, 9))

    print_matrix(matrix)

    user_answer = 0

    try:
        user_answer = int(input("> "))
    except ValueError:
        print("Incorrect format.")
    finally:
        if user_answer == determinant_count(matrix):
            print("Right")
            return 1
        print("Wrong")
        return 0
