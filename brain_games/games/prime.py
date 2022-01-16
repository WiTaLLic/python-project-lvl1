import prompt
from random import randint


def condition_prime():
    """Сonditions of the game-praime"""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def operation_prime(random_number):
    """The function determines whether the number is prime or not"""
    counter = 0
    for i in range(2, (random_number // 2) + 1):
        if (random_number % i == 0):
            counter += 1
    if (counter <= 0):
        return True
    else:
        return False

def question_prime(random_number):
    """Output of the question """
    print(f"Question: {random_number}")


def plaer_respons():
    """The function outputs the player's response """
    respon = prompt.string('Your answer: ')
    return(respon)


def reviews_prime(respons, number, names):
    """Сorrect answer game-prime"""
    if (respons == 'yes' and number) or (respons == 'no' and number is False):
        print('Correct!')
        return True

    elif (respons == 'yes' and not number) or (respons != 'no' and not number):
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'no'.\
        \nLet's try again, {names}!")
        return False

    elif (respons == 'no' and number) or (respons != 'yes' and number):
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'yes'.\
        \nLet's try again, {names}!")
        return False


def game_prime(NUMBER_QUESTIONS, names):
    """ Start game-prime"""

    random_number = randint(1, 100)

    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question_prime(random_number)
    respons = plaer_respons()
    prime_number = operation_prime(random_number)
    correct_input = reviews_prime(respons, prime_number, names)

    if correct_input is not True:
        return

    game_prime(NUMBER_QUESTIONS, names)
