import prompt
from random import randint


def condition_gcd():
    """Сonditions of the game_gcd"""
    print('Find the greatest common divisor of given numbers.')


def operation_gcd(random_number_one, random_number_two):
    """Search for gcd of two numbers """
    if(random_number_two == 0):
        return random_number_one
    else:
        return operation_gcd(
            random_number_two,
            random_number_one % random_number_two)


def question_gcd(random_number_one, random_number_two):
    """Сreate two random numbers to find the gcd """
    print(f"Question: {random_number_one} {random_number_two}")


def plaer_respons():
    """The function outputs the player's response """
    respon = prompt.string('Your answer: ')
    return(respon)


def reviews_gcd(respons, gcd_result, names):
    """Сorrect answer game-gcd"""
    if respons == str(gcd_result):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{gcd_result}'.\
        \nLet's try again, {names}!")
        return False


def game_gcd(NUMBER_QUESTIONS, names):
    """ Start game-gcd """
    random_number_one = randint(0, 100)
    random_number_two = randint(0, 100)

    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question_gcd(random_number_one, random_number_two)
    respons = plaer_respons()
    gcd_result = operation_gcd(random_number_one, random_number_two)
    correct_input = reviews_gcd(respons, gcd_result, names)

    if correct_input is not True:
        return

    game_gcd(NUMBER_QUESTIONS, names)
