#Short Answers
#Question 1
#You can reuse the same statements just by calling a single function so you don't have to re-write lines of code

#Question 2
#def main():
#you are defining the function with the name "main()" as the header and afterwards you have the chunk of code

#Question 3
#If it is a function with a loop, it will repeat until the stop condition is met or if it is a while True loop, it repeats until you enter the input set to quit the loop

#Question 4
#Local variables are variables that are defined inside a variable and only that specific variable can access it. i.e.

def main():
    number = 10
    show_number()
def show_number():
    #number is a local variable to "main() and does not have access to it"
    print(number)
main()

#Question 5
#As stated in the previous answer, the scope of a local variable is just the function/statement it is defined in. 

#Question 6
#If a global variable has the same name as a local variable, it could override the local variable making it difficult to debug
#at least in my previous experience with Javascript and C#

#Question 7
#You would use randint() to get a random number from the library of [0, 5, 10, 15, 20, 25]

#Question 8
#The following statement is a value returning function

def returnNum():
    a = int(input("give me a number"))
    b = a**3
    return b
    #here you return the value of "b"
returnNum()

#Question 9
#IPO
    #Input, Processing, Output. 
    #It lists what the input it, how it is processed, and what the output is and why that is the output

#Question 10
#A bool function is something that return True or False

def boolFunction():
    a = 5
    b = 2
    print(b > a)
    #This will return False
    print(a > b)
    #This returns True
boolFunction() 

#Question 11
#instead of working with the large program itself, if you break it down into modules, you do work on each section 
