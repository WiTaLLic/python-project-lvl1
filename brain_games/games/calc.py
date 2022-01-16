import prompt
from random import randint, choice


def conditions_calc():
    """Сonditions of the game-calc"""
    return print('What is the result of the expression?')


def question_calc(number_one, math_operator, number_two):
    """Random selection of two operands and an operator"""
    print(f"Question: {number_one} {math_operator} {number_two}")


def plaer_respons():
    """The function outputs the player's response """
    respon = prompt.string('Your answer: ')
    return(respon)


def reviews_calc(respons, calc_result, names):
    """Сorrect answer game-calc"""
    if respons == str(calc_result):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{calc_result}'.\
            \nLet's try again, {names}!")
        return False


def operation(random_number_one, random_math_operator, random_number_two):
    """Performing an operation by operator """
    if random_math_operator == '+':
        calculation_result = random_number_one + random_number_two
    if random_math_operator == '-':
        calculation_result = random_number_one - random_number_two
    if random_math_operator == '*':
        calculation_result = random_number_one * random_number_two
    return (calculation_result)


def game_calc(NUMBER_QUESTIONS, names):
    """ Start game-calc """
    random_number_one = randint(0, 100)
    random_math_operator = choice('+-*')
    random_number_two = randint(0, 100)

    
    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question_calc(
        random_number_one,
        random_math_operator,
        random_number_two
    )

    respons = plaer_respons()
    calc_result = operation(
        random_number_one,
        random_math_operator,
        random_number_two
    )
    correct_input = reviews_calc(respons, calc_result, names)

    if correct_input is not True:
        return

    game_calc(NUMBER_QUESTIONS, names)
