"""Variable for 'all' characters that are not allowed"""
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}[]*/+-_=',.`"


def addition(matrix_1, matrix_2, solved_matrix):
    """Function to add two matrix"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix_1)) if elem in ALPHABET]
    if check:
        return False
    for i, val in enumerate(matrix_1):
        for k in range(len(val)):
            solved_matrix.append(int(val[k]) + int(matrix_2[i][k]))


def multiplication_by_constant(constant, matrix_1, solved_matrix):
    """Mulptiplication by a constant"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix_1)) if elem in ALPHABET]
    if check:
        print("You typed letters")
        return False
    for i, val in enumerate(matrix_1):
        for k in range(len(val)):
            solved_matrix.append(float(val[k]) * constant)


def multiplication(matrix_1, matrix_2):
    """Function to multiply two matrix"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix_1)) if elem in ALPHABET]
    check_s = [elem for elem in (''.join(''.join(x) for x in matrix_2)) if elem in ALPHABET]
    if check or check_s:
        return False
    m_1_len = len(matrix_1)
    m_2_len = len(matrix_2)
    m_2_0_len = len(matrix_2[0])

    result = [[None for i in range(m_2_0_len)] for i in range(m_1_len)]  # c: m × k

    for i in range(m_1_len):
        for j in range(m_2_0_len):
            result[i][j] = sum(int(matrix_1[i][s]) * int(matrix_2[s][j]) for s in range(m_2_len))
    return result


def transpose(argument, matrix_1):
    """Function to transpose matrix"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix_1)) if elem in ALPHABET]
    if check:
        return False
    result = []
    match argument:
        case 1:
            result = list(map(list, zip(*matrix_1)))
        case 2:
            result = list(reversed(matrix_1))
            result = list(map(list, zip(*result)))
            result = list(reversed(result))
        case 3:
            for i in range(len(matrix_1)):
                result.append(list(reversed(matrix_1[i])))
        case 4:
            result = list(reversed(matrix_1))
    return result

def minor(matrix, i, j):
    """Finding minor of matrix"""
    tmp = [row for k, row in enumerate(matrix) if k != i]
    # print(f" tmp 1 is {tmp}")
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    # print(f" tmp 2 is {tmp}")
    return tmp

def determinant_count(matrix):
    """Starts process of finding determinant of matrix"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix)) if elem in ALPHABET]
    if check:
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

def inverse(matrix):
    """Making inversed matrix"""
    check = [elem for elem in (''.join(''.join(x) for x in matrix)) if elem in ALPHABET]
    if check:
        return False
    result = []
    for i in range(len(matrix)):
        inter_result = []
        for k in range(len(matrix[i])):
            minor_sign = (-1) ** (i + k)
            inter_result.append(determinant_count(minor(matrix, i, k)) * minor_sign)
        for i, val in enumerate(inter_result):
            val = float(val)
        result.append(inter_result)
    for i in range(len(result)):
        for k in range(len(result[i])):
            result[i][k] = (float("{:.2f}".format(result[i][k] * (1/determinant_count(matrix)))))
    return transpose(1, result)
#DeFakto
