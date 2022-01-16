import prompt
from brain_games.games.calc import *
from brain_games.games.even import *

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
    
    

