from brain_games.quest import question
from brain_games.respons import plaer_respons
from brain_games.review import reviews
from random import randint


def game(NUMBER_QUESTIONS, names):
    """ Start game """
    random_number = randint(0, 100)

    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        return

    NUMBER_QUESTIONS -= 1

    question(random_number)
    respons = plaer_respons()

    if random_number % 2 != 0 and respons == 'yes':
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \
            Let's try again, {names}!")
        return
    elif random_number % 2 == 0 and respons == 'no':
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \
            Let's try again, {names}!")
        return
    elif random_number % 2 == 0 and respons != 'yes':
        print(f"'{respons}' is wrong answer ;(. Correct answer was 'yes'. \
            Let's try again, {names}!")
        return
    elif random_number % 2 != 0 and respons != 'no':
        print(f"'{respons}' is wrong answer ;(. Correct answer was 'no'. \
            Let's try again, {names}!")
        return
    reviews(random_number, respons)
    game(NUMBER_QUESTIONS, names)
