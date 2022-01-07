#!/usr/bin/env python
from brain_games.games.even import welcom_to_game
from brain_games.games.even import welcom_user
from brain_games.games.even import conditions_even
from brain_games.games.even import game
from brain_games.games.even import NUMBER_QUESTIONS


def main():
    welcom_to_game()
    nam = welcom_user()
    conditions_even()

    game(NUMBER_QUESTIONS, nam)


if __name__ == '__main__':
    main()
