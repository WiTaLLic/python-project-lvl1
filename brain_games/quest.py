def question(random_number):
    """Random choice of question """
    print(f"Question: {random_number}")


def question_calc(random_number_one, random_math_operator, random_number_two):
    """Random selection of two operands and an operator"""
    print(f"Question: {random_number_one} {random_math_operator} \
    {random_number_two}")


def question_gcd(random_number_one, random_number_two):
    """Сreate two random numbers to find the gcd """
    print(f"Question: {random_number_one} {random_number_two}")


def question_prograssion(random_START, STOP, random_STEP, hidden_number):
    """Аrithmetic progression output """
    print('Question: ', end=' ')
    for i in range(random_START, STOP, random_STEP):
        if i == hidden_number:
            print('..', end=' ')
        else:
            print(i, end=' ')
    print()
