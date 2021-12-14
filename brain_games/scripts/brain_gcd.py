from brain_games.games.quest import question_gcd
from brain_games.games.respons import plaer_respons
from brain_games.games.review import reviews_calc
from brain_games.games.math_operation import operation_gcd
from random import randint


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
    correct_input = reviews_calc(respons, gcd_result, names)

    if correct_input is not True:
        return

    game_gcd(NUMBER_QUESTIONS, names)
