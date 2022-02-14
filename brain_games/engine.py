


def welcom_user():
    """Ask the player for a name and print a greeting """
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name