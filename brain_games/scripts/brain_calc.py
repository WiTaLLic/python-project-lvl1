#!/usr/bin/env python
from brain_games.games.calc import welcom_to_game
from brain_games.games.calc import welcom_user
from brain_games.games.calc import conditions_calc
from brain_games.games.calc import game_calc
from brain_games.games.even import NUMBER_QUESTIONS


def main():
    welcom_to_game()
    name = welcom_user()
    conditions_calc()

    game_calc(NUMBER_QUESTIONS, name)


if __name__ == '__main__':
    main()
