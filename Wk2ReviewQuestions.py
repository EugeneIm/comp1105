import turtle
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
#1
#User enters their height and asigns the value to a variable called "height". 

def main():
    height = input("Please enter your height: ")
    height = height
    print("Your height is: " + height + "cm")

main()

#2
#User enters a color and asigns the value to a variable called "color"

def main():
    color = input("Please enter your favorite color: ")
    color = color
    print("Your favorite color seems to be " + color)

main()

#3
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

#4
#Variables w = 5, x = 4, y = 8, and z = 2
w = 5
x = 4
y = 8
z = 2

def main():
    result_a = x + y
    print("a = " + str(result_a))
    result_b = z * 2
    print("b = " + str(result_b))
    result_c = y / x
    print("c = " + str(result_c))
    result_d = y - z
    print("d = " + str(result_d))
    result_e = w // z
    print("e = " + str(result_e))

main()

#5
#Write a statement that assigns the values of 10 and 14 to a vairable called "total"
x = 10
y = 14
total = x + y
def main():
    print("The value of 'total' is: " + str(total))

main()

#6
#Subtracts the variable "down_payment" from the variable "total" and assigns that value to "due"

def main():
   total = int(input("What is the total? "))
   total = total
   down_payment = int(input("Please enter the value of the down payment: "))
   down_payment = down_payment
   due = total - down_payment

   print("The amount due is: " + str(due))

main()

#7
#Multiply the variable "subtotal" by 0.15 and assign that to "total"

def main():
    subtotal = float(input("What is the subtotal?"))
    subtotal = subtotal
    total = subtotal * 0.15
    print("Total value of 'total' is: " + str(total))
main()

#8
#What would the following display?
a = 5
b = 2
c = 3
result = a + b*c
print(result)
#result = 11 because 2*3 has precedence over addition. 
#hence (2*3) + 5 = 6 + 5 = 11

#9
#What would the following display?
num = 99
num = 55
print(num)
#Prints out 55 because it goes from top to bottom and the second assignment of "num" overrides the previous which was 99. So now when it gets to the print function, the previous assignment, 99 was overridden by the assignment 55. 


#10
#Variable sales_reference is a float value, limit the float value rounded to two decimal places
sale_a = 3.1182
sale_b = 4.298445
sales_total = sale_a + sale_b
sales_reference = round(sales_total, 2)
print(sales_reference)
#use the 'round' function to round the number to two decimal places

#11
#number = 1234567.456, write a statement that formats the value to 1,234,567.5

def main():
    number = 1234567.456
    print("Result : {:,.1f}".format(number))
    #{:,.1f} does the following to the number
    #The "," separates the number into the thousands, etc. 
    #The "." is just for the decimal point so it's a float and not an int
    #1f is the decimal point to 1 digit and rounded. 
main()

#12
#What will the following display?

print('George', 'John', 'Paul', 'Ringo', sep='@')
#George@John@Paul@Ringo

#13
#Write a turtle graphics that draws a circle with a radius of 75 px. 
t = turtle.Turtle()
r = 75
t.circle(r)

#14
#Turtle graphics to write a square that is 100px wide on all sides and filled with the color blue.

#15
#Turtle graphics statement to draw a 100px^2 square and a circle centered inside.
#Circle radius will be 80px and filled red. The square will not be filled with red. 

