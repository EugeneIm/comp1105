import random
import string
#lab 6 questions and answers
#Write a statement that does the following:
'''
1. Generate a random int between -50 and 50 inclusive
2. Random int between -50 and 50 exclusive
3. Random int deivisible by 3 between -50 and 50 inclusive
4. Random float between -50.00 and 50.00 inclusive
'''

#Q1 pt 1.
def ran_inclusive():
    #random int between -50 and 50 inclusive
    ran_num = random.randint(-50, 50)
    print(ran_num)
ran_inclusive()

#Q1 pt 2.
def ran_exclusive():
    ran_num = random.randint(-49, 49)
    print(ran_num)
ran_exclusive()

#Q1 pt 3.
def ran_divisible():
    ran_div = random.randint(-50, 50)
    if ran_div % 3 == 0:
        print(ran_div)
    else:
        print(ran_div , "is not divisible by 3")
ran_divisible()

#Q1 pt 4.
def ran_float():
    ran_float = random.uniform(-50.00, 50.00)
    print(format(ran_float, '.2f'))
ran_float()

#Q2
#Function to generate a random capital letter

def letter():
    ran_letter = random.choice(string.ascii_letters)
    print(ran_letter.title())
letter()

#Q3 
#Generate and return a random letter.

def ran_letter():
    letter = random.choice(string.ascii_letters)
    print(letter.lower())
ran_letter()
