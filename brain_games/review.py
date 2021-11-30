def reviews(random_number, respons):
    """Сorrect answer"""
    if random_number % 2 == 0 and respons == 'yes':
        print('Correct!')
    elif random_number % 2 != 0 and respons == 'no':
        print('Correct!')
    