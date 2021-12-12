def operation(random_number_one, random_math_operator, random_number_two):
    """Performing an operation by operator """
    if random_math_operator == '+':
        calculation_result = random_number_one + random_number_two
    if random_math_operator == '-':
        calculation_result = random_number_one - random_number_two
    if random_math_operator == '*':
        calculation_result = random_number_one * random_number_two
    return (calculation_result)


def operation_gcd(random_number_one, random_number_two):
    """Search for gcd of two numbers """
    if(random_number_two == 0):
        return random_number_one
    else:
        return operation_gcd(
            random_number_two,
            random_number_one % random_number_two)


def operation_prime(random_number):
    """The function determines whether the number is prime or not"""
    counter = 0
    for i in range(2, (random_number // 2) + 1):
        if (random_number % i == 0):
            counter += 1
    if (counter <= 0):
        return True
    else:
        return False
