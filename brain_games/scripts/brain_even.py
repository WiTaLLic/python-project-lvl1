#!/usr/bin/env python
from brain_games.salute import welcom_user
from brain_games.games import game


NUMBER_QUESTIONS = 3


def main():
    print("Welcom to the Brain Games!")

    names = welcom_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    game(NUMBER_QUESTIONS, names)


if __name__ == '__main__':
    main()
