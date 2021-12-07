def operation(random_number_one, random_math_operator, random_number_two):
    """Performing an operation by operator """
    if random_math_operator == '+':
        calculation_result = random_number_one + random_number_two
    if random_math_operator == '-':
        calculation_result = random_number_one - random_number_two
    if random_math_operator == '*':
        calculation_result = random_number_one * random_number_two
    return (calculation_result)
