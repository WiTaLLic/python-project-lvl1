import prompt
from brain_games.games.calc import *
from brain_games.games.even import *
from brain_games.games.gcd import *
from brain_games.games.progression import *
from brain_games.games.prime import *

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
    
    

