import prompt

def welcom_user():
	"""The function asks for user data"""
	name = prompt.string('May I have your name? ')
	print(f"Hello, {name}!")
