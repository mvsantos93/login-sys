def check_input():
	print("""
These are the available commands:
'add' to add a new username and password
'login' to login
'check' to check all users created
'exit' to exit this program
	""")
	
	cmd = input("What is your command?> ")
	if cmd == "add":
		return add_user()
	elif cmd == "login":
		return login()
	elif cmd == "check":
		return check_user()
	elif cmd == "exit":
		exit()
	else:
		print("Invalid input. Please try again!")
		return check_input()

def login():
	username = input("Enter your username: ")
	if username in users:
		password = input(f"Hello {username}, please enter your password: ")
		if users[username] == password:
			print("Succesful login!")
			return check_input()
		else:
			print("Incorrect password, please try again!")
			return login()
	else:
		print(f"No {username} found! Create or try again!")
		return check_input()

def check_user():
	print("These are the currently usernames registered:")
	for x in users:
		print(x)
	return check_input()

class add_user():
	def __init__(self):
		self.user_n = input("Enter a new username: ")
		self.user_p = input("Enter a new password for your username: ")
		users[self.user_n] = self.user_p
		print("Username and password succesfully created!")
		return check_input()

users = {}
check_input()