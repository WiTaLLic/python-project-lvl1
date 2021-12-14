from brain_games.scripts.brain_calc import game_calc
from brain_games.scripts.brain_even import game
from brain_games.scripts.brain_gcd import game_gcd
from brain_games.scripts.brain_prime import game_prime
from brain_games.scripts.brain_progression import game_progression


def starting_game(name_game, NUMBER_QUESTIONS, names):
    """Starting the selected game """
    if name_game == 'brain-even':
        return game(NUMBER_QUESTIONS, names)
    if name_game == 'brain-calc':
        return game_calc(NUMBER_QUESTIONS, names)
    if name_game == 'brain-gcd':
        return game_gcd(NUMBER_QUESTIONS, names)
    if name_game == 'brain-prime':
        return game_prime(NUMBER_QUESTIONS, names)
    if name_game == 'brain-progression':
        return game_progression(NUMBER_QUESTIONS, names)
