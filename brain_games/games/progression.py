import prompt
from random import randint, randrange


def condition_progression():
    """Сonditions of the game-progression"""
    print('What number is missing in the progression?')


def question_prograssion(random_START, STOP, random_STEP, hidden_number):
    """Аrithmetic progression output """
    print('Question:', end=' ')
    for i in range(random_START, STOP, random_STEP):
        if i == hidden_number:
            print('..', end=' ')
        else:
            print(i, end=' ')
    print()


def plaer_respons():
    """The function outputs the player's response """
    respon = prompt.string('Your answer: ')
    return(respon)


def reviews_progression(respons, hidden_number, names):
    """Сorrect answer game-progression"""
    if respons == str(hidden_number):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{hidden_number}'.\
        \nLet's try again, {names}!")
        return False


def game_progression(NUMBER_QUESTIONS, names):
    """ Start game-progression """
    STOP = 35

    random_START = randint(0, 5)
    random_STEP = randint(1, 5)
    hidden_number = randrange(random_START, STOP, random_STEP)

    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question_prograssion(random_START, STOP, random_STEP, hidden_number)
    respons = plaer_respons()
    correct_input = reviews_progression(respons, hidden_number, names)

    if correct_input is not True:
        return

    game_progression(NUMBER_QUESTIONS, names)
