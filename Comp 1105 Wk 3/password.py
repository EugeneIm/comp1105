while True:
	password = "password"

	new_password = str(input("Try and figure out the password: "))

	if new_password == password:
		print("Congratulations you cracked the password")
	if new_password == "quit":
		break
	else:
		print("Try again or enter 'quit' to stop")
	
