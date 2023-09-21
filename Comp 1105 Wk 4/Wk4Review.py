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

def main():
 ROCK = 0
 SCiSSORS = 1
 PAPER = 2
 p1 = int(input("@Player1 - Select rock(0), scissors (1), or paper(2): "))
 p2 = int(input("@Player2 - Select rock(0), scissors (1), or paper(2): "))
 if p1 < 0 or p1 > 2 or p2 < 0 or p2 > 2 :
     print("DATA ERROR: enter 0, 1 0r 2 as inputs!")
 else: # p1 and p2 are valid numbers
    if p2 == ROCK :
        if p1 == ROCK:
            print("Player2 is rock. Pleyer1 is rock. It is draw.")
    elif p1 == SCiSSORS:
        print("Player2 is rock. Pleyer1 is scissors. Player2 won!")
    else : #p1 is paper
        print("Player2 is rock. Pleyer1 is paper. Player1 won!")
    if p2 == PAPER :
        if p1 == ROCK:
            print("Player2 is paper. Pleyer1 is rock. Player2 won!")
        elif p1 == SCiSSORS:
            print("Player2 is paper. Pleyer1 is scissors. Player1 won!")
    else : #p1 is paper
        print("Player2 is paper. Pleyer1 is paper. It is draw.")
    if p1 == ROCK:
        print("Player2 is scissors. Pleyer1 is rock. Player1 won!")
    elif p1 == SCiSSORS:
        print("Player2 is scissors. Pleyer1 is scissors. It is draw.")
    else : #p1 is paper
        print("Player2 is scissors. Pleyer1 is paper. Player2 won!")
#calling main function
main()

#Very inefficient

#More efficient RPS on Wk4.py