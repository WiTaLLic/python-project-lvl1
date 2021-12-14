from brain_games.games.quest import question
from brain_games.games.respons import plaer_respons
from brain_games.games.review import reviews
from random import randint


def game(NUMBER_QUESTIONS, names):
    """ Start game """
    random_number = randint(0, 100)

    
    

    NUMBER_QUESTIONS -= 1

    question(random_number)
    
    respons = plaer_respons()

    reviews(random_number, respons, names)

    game(NUMBER_QUESTIONS, names)
