from brain_games.games.quest import question_prime
from brain_games.games.respons import plaer_respons
from brain_games.games.review import reviews_prime
from brain_games.games.math_operation import operation_prime
from random import randint


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
