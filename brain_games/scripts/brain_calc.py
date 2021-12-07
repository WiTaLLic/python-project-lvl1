#!/usr/bin/env python
from brain_games.salute import welcom_user
from brain_games.games import game_calc
from brain_games.conditions_games import conditions_calc


NUMBER_QUESTIONS = 3


def main():
    print("Welcom to the Brain Games!")

    names = welcom_user()

    conditions_calc()

    game_calc(NUMBER_QUESTIONS, names)


if __name__ == '__main__':
    main()
