"""Connecting module sys and file calculations.py"""
import sys
import calculations
MATRIX_1_WIDTH, MATRIX_1_HEIGHT, MATRIX_2_WIDTH, MATRIX_2_HEIGHT = (0, 0, 0, 0)
matrix_1, matrix_2, solved_matrix, MATRIX_FOR_PRINT = ([], [], [], [])


def func_chunk(lst, numb):
    """Сonverting an ordinary list into a two-dimensional one"""
    numb = int(numb)
    for i in range(0, len(lst), numb):
        result = lst[i: numb + i]

        if len(result) < numb:
            result += [None for y in range(numb - len(result))]
        yield result


def format_matrix(matrix_user, matrix_x):
    """Values for layers"""
    print("Enter like this : 1 2 3 4 n")
    matrix_x = int(matrix_x)
    for _ in range(0, matrix_x * matrix_x, matrix_x):  # Formatting user data for each layer
        user_layer = input(">")
        matrix_user.append(user_layer.split())


def get_values(action):
    """Getting values of each layer"""
    global MATRIX_1_WIDTH,MATRIX_1_HEIGHT,MATRIX_2_WIDTH,MATRIX_2_HEIGHT
    MATRIX_1_HEIGHT = input("Height").split(" ")[-1]
    MATRIX_1_WIDTH = input("Width").split(" ")[-1]
    format_matrix(matrix_1, MATRIX_1_HEIGHT)
    if action in ('add', 'multiply matrices'):
        MATRIX_2_HEIGHT = input("Height").split(" ")[-1]
        MATRIX_2_WIDTH = input("Width").split(" ")[-1]
        format_matrix(matrix_2, MATRIX_2_HEIGHT)
    return matrix_1, matrix_2


def get_matrix(user_choice):
    """All cases"""
    global MATRIX_FOR_PRINT
    match user_choice:
        case 1:
            try:
                matrix_1, matrix_2 = get_values("add")
            except TypeError:
                print("You 've typed non number!!!")
            else:
                if (MATRIX_1_WIDTH != MATRIX_2_WIDTH) or (MATRIX_1_HEIGHT != MATRIX_2_HEIGHT):
                    print("The operation cannot be performed.")
                else:
                    calculations.addition(matrix_1, matrix_2, solved_matrix)
                    MATRIX_FOR_PRINT = list(func_chunk(solved_matrix, MATRIX_1_WIDTH))
        case 2:
            try:
                constant = float(input("Input the number for multiplication "))
            except ValueError:
                print("You have typed non number")
            else:
                try:
                    matrix_1, matrix_2 = get_values("nothing")
                except TypeError:
                    print("You 've typed non number!!!")
                else:
                    calculations.multiplication_by_constant(constant, matrix_1, solved_matrix)
                    MATRIX_FOR_PRINT = list(func_chunk(solved_matrix, MATRIX_1_WIDTH))
        case 3:
            try:
                matrix_1, matrix_2 = get_values("multiply matrices")
            except TypeError:
                print("You 've typed non number!!!")
            else:
                if (MATRIX_1_WIDTH != MATRIX_2_HEIGHT) or (MATRIX_1_HEIGHT != MATRIX_2_WIDTH):
                    print("You 've input wrong size")
                else:
                    MATRIX_FOR_PRINT = calculations.multiplication(matrix_1, matrix_2)
        case 4:

            print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
            # choice_trans = 0
            try:
                choice_trans = int(input("Your choice: > "))
            except TypeError:
                print("Input only integers")
            try:
                matrix_1, matrix_2 = get_values("nothing")
            except TypeError:
                print("Toy 've typed non number!!!")
            else:
                MATRIX_FOR_PRINT = calculations.transpose(choice_trans, matrix_1)
        case 5:
            try:
                matrix_1, matrix_2 = get_values("nothing")
            except TypeError:
                print("You 've typed non number!!!")
            else:
                result = calculations.determinant_count(matrix_1)
                print(result)
        case 6:
            try:
                matrix_1, matrix_2 = get_values("nothing")
            except TypeError:
                print("You 've typed non number!!!")
            else:
                MATRIX_FOR_PRINT = calculations.inverse(matrix_1)
        case _:
            print("You have typed something wrong!")


def print_matrix(matrix):
    """Print matrix the way to comfortable see it"""
    for ind, val in enumerate(matrix):
        for k in range(len(val)):
            print(val[k], end=' ')
        print()

def hello_scene():
    """Greetings to user"""
    try:
        user_choice = int(input(">"))
    except ValueError:
        print("Type only integers!")
        return False
    return user_choice


if __name__ == "__main__":
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
        user_state = hello_scene()
        if not user_state:
            user_state = hello_scene()
        if user_state == 0:
            sys.exit()
        get_matrix(user_state)
        print_matrix(MATRIX_FOR_PRINT)
#DeFakto
