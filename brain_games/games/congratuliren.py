
def congratulations(NUMBER_QUESTIONS, names):
    """"""
    if NUMBER_QUESTIONS < 1:
        print(f"Congratulations, {names}!")
        NUMBER_QUESTIONS -= 1
        return False