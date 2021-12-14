import prompt
from brain_games.games.conditions_games import conditions_even, conditions_calc
from brain_games.games.conditions_games import condition_gcd, condition_prime
from brain_games.games.conditions_games import condition_progression


def name_of_the_game():
    """Game selection"""
    choose_games = prompt.string('')

    return choose_games


def what_game(names_games):
    """Сonditions for playing by name """
    if names_games == 'brain-even':
        return conditions_even()

    if names_games == 'brain-calc':
        return conditions_calc()

    if names_games == 'brain-gcd':
        return condition_gcd()

    if names_games == 'brain-prime':
        return condition_prime()

    if names_games == 'brain-progression':
        return condition_progression()
