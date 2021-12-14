from brain_games.games.quest import question_prograssion
from brain_games.games.respons import plaer_respons
from brain_games.games.review import reviews_progression
from random import randint, randrange


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
