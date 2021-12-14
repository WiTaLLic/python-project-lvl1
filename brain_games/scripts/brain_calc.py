from brain_games.games.quest import question_calc
from brain_games.games.respons import plaer_respons
from brain_games.games.review import reviews_calc
from brain_games.games.math_operation import operation
from random import choice, randint


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
