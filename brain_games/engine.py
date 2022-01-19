import prompt
from brain_games.games.calc import conditions_calc, game_calc
from brain_games.games.even import conditions_even, game_even
from brain_games.games.gcd import condition_gcd, game_gcd
from brain_games.games.progression import condition_progression
from brain_games.games.progression import game_progression
from brain_games.games.prime import condition_prime, game_prime


def start(game):

    NUMBER_QUESTIONS = 3

    print('Welcome to the Brain Games!') 

    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")

    if game == 'calc':
        conditions_calc()
        game_calc(NUMBER_QUESTIONS, name)

    if game == 'even':
        conditions_even()
        game_even(NUMBER_QUESTIONS, name)

    if game == 'gcd':
        condition_gcd()
        game_gcd(NUMBER_QUESTIONS, name)

    if game == 'progression':
        condition_progression()
        game_progression(NUMBER_QUESTIONS, name)

    if game == 'prime':
        condition_prime()
        game_prime(NUMBER_QUESTIONS, name)
