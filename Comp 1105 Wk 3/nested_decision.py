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
'''
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
'''

#a = num1 = 5 and num2 = 6. output = Hermoine, Voldemort
#b = num1 = 6 and num2 = 12. output = Fred, Voldemort
#c = num1 = 12 and num2 = 26. output = Ginny, Voldemort
#d = num1 = 3 and num2 = 3. output = Harry, Ron, Hermoine, Voldemort 

'''
if num1 >= num2:
 print("Harry")
 print("Ron")
if (num1 + 5) >= num2:
 print("Hermione")
else:
 if num2%3 == 0:
print("Fred")
 elif num2%3 == 1:
print("George")
 elif num2%3 == 2:
print("Ginny")
print("Voldemort")
'''

#864 to binary
'''
864/2 = 437 + 0
437/2 = 218 + 1
218/2 = 109 + 0
109/2 = 54 + 1
54/2 = 27 + 0
27/2 = 13 + 1
13/2 = 6 + 1
6/2 = 3 + 0
3/2 = 1 + 1
1/2 = 0
0101011010 is 864 in binary
'''

#101011100 to int 
'''
1 	^256
0	^128
1	^64
0	^32
1	^16
1	^8
1	^4
0	^2
0	^0
256+64+16+8+4 = 350
'''

#calculator program + - * %
def main():
	num1 = int(input("What is the first number? "))
	num2 = int(input("What is the second number? "))
	operator = input("How would you like to calculate it? ")

	if operator == "+":
		addValue = num1 + num2
		print(addValue)
	elif operator == "-":
		subtractValue = num1 - num2
		print("The end value is", subtractValue)
	elif operator == "*":
		multiplyValue = num1 * num2
		print("The end value is", multiplyValue)
	elif operator == "%":
		modulusValue = num1%num2
		print("The end value is", modulusValue)
	elif operator == "/":
		if num2 == 0:
			print("You cannot divide by 0")
		else:
			divisionValue = num1 / num2
			print("The end value is", format(divisionValue, ".2f"))
	else:
		print("Operator must be one of the following: +, -, /, %, or *")
main()