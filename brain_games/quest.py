def question(random_number):
    """Random choice of question """
    print(f"Question: {random_number}")


def question_calc(number_one, math_operator, number_two):
    """Random selection of two operands and an operator"""
    print(f"Question: {number_one} {math_operator} {number_two}")


def question_gcd(random_number_one, random_number_two):
    """Сreate two random numbers to find the gcd """
    print(f"Question: {random_number_one} {random_number_two}")


def question_prograssion(random_START, STOP, random_STEP, hidden_number):
    """Аrithmetic progression output """
    print('Question:', end=' ')
    for i in range(random_START, STOP, random_STEP):
        if i == hidden_number:
            print('..', end=' ')
        else:
            print(i, end=' ')
    print()


def question_prime(random_number):
    """Output of the question """
    print(f"Question: {random_number}")
