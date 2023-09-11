#True or false
'''
1. False: 
    Programmers do NOT have to worry about syntax errors because pseudocode is just what the program SHOULD do once finished. 

2. True:
    multiplication and division have precedence over addition and subtraction. 

3. True:
    Variable names cannot have spaces, however they can have underscores in place of spaces. 
    number twelve => "invalid syntax"
    number_twelve => valid syntax

4. No language can have a variable which starts with a number. 
    - Cannot assign to literal
    
    12 = "twelve"
    print(12)

5. "efficiency is not defined" So a variable that is not assigned anything will stop the compiler. 
'''

#Short Answers
'''
1. What does a professional programmer do first to gain an understanding of a problem? 
    - When you read the problem, usually at higher levels where you work with multiple variable in multiple sections, the compiler SHOULD tell you where the error is and what the general problem is. 
    - For example, the previous error, "efficiency is not defined", the compiler tells you that efficiency doesn't have anything assigned to it. 

2. What is pseudcode?
    - Pseudocode is essentially an overview of what the finished product should do (if there are no errors) once finished. 

3. Computer programs typically perform what three steps?
    - Input
    - Processing
    - Output

4. If a math expression adds a float to an int, what will be the result?
    - Since they are both technically integers, you can add a float to an int and it will be converted to a float. 
    x = 0.2
    y = 1
    print(x+y)

5. What is the difference between float point division and int division?
    - Float division will return, a float
    - Int division will only return a whole number

6. What is a magic number? Why are they problematic?
    - A magic number doesn't have to be assigned to anything which leads to confusion in the code. 
    i.e.
    KM = 1000
    KM/100 = 100. 
    print(KM/100)
    Where did the "100" come from? It still works, the function still works but WHERE DID THE 100 COME FROM?

7. Const Pi = 3.14159. Advantage of "const" vs using 3.14159 in multiple functions? 
    - Since you've already assigned the float "3.14159" to "Pi", you can use "Pi" anywhere as long as it's valid. 
'''

#Algorithm Workbench

#User enters their height and asigns the value to a variable called "height". 
'''
def main():
    height = input("Please enter your height: ")
    height = height
    print("Your height is: " + height + "cm")

main()
'''
#User enters a color and asigns the value to a variable called "color"
'''
def main():
    color = input("Please enter your favorite color: ")
    color = color
    print("Your favorite color seems to be " + color)

main()
'''
#Statements that does the following with variables a, b, c
    #adds 2 to variable a and the result is variable b

def main():
   a = int(input("Please enter the value of a: "))
   a = a
   b = a + 2
   print("the end value of b is: " + str(b))

main()

#multiplies b by 4 and assigns the result to a
def main():
    b = int(input("Please enter the value of b: "))
    b = b
    a = b * 4
    print("the end value of a is: " + str(a))

main()

#Divides a by 3.14 and assigns the result to b
def main():
    a = float(input("Please enter the value of a: "))
    a = a
    b = a / 3.14
    print("the end value of a is: " + str(b))

main()

#Subtracts 8 from b and assigns the result to a
def main():
    b = int(input("Please enter the value of b: "))
    b = b
    a = b - 8
    print("The end value of a is: " + str(a))

main()