#Lab 3

#Q1
'''
Which of the following are correct?

statement A:
if age < 16:
    print("You're ineligible for a drivers license")
if age >= 16:
    print("You can get a drivers license")

statement B:
if age < 16:
    print("Cannot get a drivers")
else:
    print("You can get a license")

both statements are correct, HOWEVER, statement A is less efficient
'''

#Q2
'''
Boolean expression using logical operators to express the following conditions:

Condition  = |x - 5| < 4.5           |x - 5| > 4.5
Expression = x < 9.5 and x > 0.5     x > 9.5 or x < 0.5 
'''

#Q3
'''
A. if isPrime = True: (Use == instead of =)
B. if isPrime == True: (Correct because you're using ==)
C. if isPrime: (Correct because you're saying if it's a prime, ...)
D. if not isPrime = False: (You need to use == to check for exact comparison)
E. if not isPrime == False: 
'''

#Q4
'''
What is the value of the expression 50 <= x <= 100 in Python if x is 45, 67, or 101

45 = False (x < 50)
67 = True (x > 50 and x < 100)
101 = False (x > 100)
'''

#Q5
'''
if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
    else:
        print("x is", x)

x = 3 and y = 2
output: x is 3

x = 3 and y = 4
output: z = 7

x = 2 and y = 2
output: ____
'''