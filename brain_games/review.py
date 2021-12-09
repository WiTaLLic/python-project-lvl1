def reviews(random_number, respons):
    """Сorrect answer"""
    if random_number % 2 == 0 and respons == 'yes':
        print('Correct!')
    elif random_number % 2 != 0 and respons == 'no':
        print('Correct!')


def reviews_calc(respons, calc_result, names):
    """Сorrect answer game-calc"""
    if respons == str(calc_result):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{calc_result}'.\
            \nLet's try again, {names}!")
        return False


def reviews_gcd(respons, gcd_result, names):
    """Сorrect answer game-gcd"""
    if respons == str(gcd_result):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{gcd_result}'.\
        \nLet's try again, {names}!")
        return False


def reviews_progression(respons, hidden_number, names):
    """Сorrect answer game-progression"""
    if respons == str(hidden_number):
        print('Correct!')
        return True
    else:
        print(f"'{respons}' is  wrong answer ;(. Correct answer was '{hidden_number}'.\
        \nLet's try again, {names}!")
        return False


def reviews_prime(respons, prime_number, names):
    """Сorrect answer game-prime"""
    if (respons == 'yes' and prime_number is True) or (respons == 'no' and prime_number is False):
        print('Correct!')
        return True

    elif (respons == 'yes' and prime_number is False) or (respons != 'no' and prime_number is False):
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'no'.\
        \nLet's try again, {names}!")
        return False

    elif (respons == 'no' and prime_number is True) or (respons != 'yes' and prime_number is True):
        print(f"'{respons}' is  wrong answer ;(. Correct answer was 'yes'.\
        \nLet's try again, {names}!")
        return False
