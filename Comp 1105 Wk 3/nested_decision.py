#salary = int(input("What is your salary? "))
#years_on_the_job = int(input("How long have you been working at this company? "))

#nested if statements for a qualification of a loan
'''
def main():
	salary = int(input("What is your current salary? "))
	years_on_the_job = int(input("How long have you worked here? "))
	if (salary < 30000) and (years_on_the_job > 2):
		print("You must have an annual salary of 30,000 or more")
	if (salary > 30000) and (years_on_the_job < 2):
		print("You must have had to work here for more 2 years")
	if (salary > 30000) and (years_on_the_job > 2):
		print("You qualify for the loan")
main()
'''

#Palindrome checker
def palindrome():

	num = int(input("Give me 3 digits "))
	if num < 100 or num > 999:
		print("number cannot be below 100 or above 999")
	else:
		if num % 10 == num // 100:
			print(num, " is a palindrome")
		else:
			print(num, " is not a palindrome")

palindrome()
