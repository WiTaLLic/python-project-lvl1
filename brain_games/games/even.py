import prompt
from random import randint


def conditions_even():
    """Сonditions of the game-even"""
    print('Answer "yes" if the number is even, otherwise answer "no"')


def question(random_number):
    """Random choice of question """
    print(f"Question: {random_number}")


def plaer_respons():
    """The function outputs the player's response """
    respon = prompt.string('Your answer: ')
    return(respon)


def reviews(random_number, respons, names):
    """Сorrect answer"""
    if random_number % 2 == 0 and respons == 'yes':
        print('Correct!')
        return True
    if random_number % 2 != 0 and respons == 'no':
        print('Correct!')
        return True
    if random_number % 2 == 0 and respons != 'yes':
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'yes'.\
            \nLet's try again, {names}!")
        return False
    if random_number % 2 != 0 and respons != 'no':
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'no'.\
            \nLet's try again, {names}!")
        return False


def game_even(NUMBER_QUESTIONS, names):
    """ Start game """
    random_number = randint(0, 100)

    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question(random_number)

    respons = plaer_respons()

    corect_input = reviews(random_number, respons, names)

    if corect_input is not True:
        return

    game_even(NUMBER_QUESTIONS, names)
