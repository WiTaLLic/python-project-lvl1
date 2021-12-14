#!/usr/bin/env python
from brain_games.games.choose_game import name_of_the_game, what_game
from brain_games.games.salute import welcome_to_game, welcom_user
from brain_games.games.start_game import starting_game



NUMBER_QUESTIONS = 3


def main():
    name_game = name_of_the_game()

    welcome_to_game()

    names = welcom_user()

    what_game(name_game)

    starting_game(name_game, NUMBER_QUESTIONS, names)
    

if __name__ == '__main__':
    main()
