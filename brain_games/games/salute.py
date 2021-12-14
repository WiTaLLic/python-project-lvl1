import prompt


def welcome_to_game():
    print("Welcom to the Brain Games!")


def welcom_user():
    """The function asks for user data"""
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
