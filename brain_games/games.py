from brain_games.quest import question, question_calc
from brain_games.quest import question_gcd, question_prograssion
from brain_games.quest import question_prime
from brain_games.respons import plaer_respons
from brain_games.review import reviews, reviews_calc, reviews_progression
from brain_games.review import reviews_prime
from brain_games.math_operation import operation, operation_gcd
from brain_games.math_operation import operation_prime
from random import choice, randint, randrange


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
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.)\
        Let's try again, {names}!")
        return
    elif random_number % 2 == 0 and respons == 'no':
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'.)\
        Let's try again, {names}!")
        return
    elif random_number % 2 == 0 and respons != 'yes':
        print(f"'{respons}' is wrong answer ;(. Correct answer was 'yes'.)\
        Let's try again, {names}!")
        return
    elif random_number % 2 != 0 and respons != 'no':
        print(f"'{respons}' is wrong answer ;(. Correct answer was 'no'.)\
        Let's try again, {names}!")
        return
    reviews(random_number, respons)
    game(NUMBER_QUESTIONS, names)


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


def game_progression(NUMBER_QUESTIONS, names):
    """ Start game-progression """
    STOP = 30

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
