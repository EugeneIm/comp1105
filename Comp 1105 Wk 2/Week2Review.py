#print('this is the week 2 notes/questions/answers')
#do numbers 2, 4, 6, 9, 11, and 12. 

#Question 2
#– What is the type of each variable after running each statement:
#Num1
    #inputs are always a string so it is a string
    #to change the string to something else you can use int(input) or float(input), etc. 

#Num2
    #int(input("...")) has been converted to the data type of int so if you were to do the following
        #hour = int(input("12"))
        #print(hour) => the output will be an int

#Num3    
    #float(input("...")) has been converted to the data type of float because of the "float(input("...")), etc. 

#Num4
    #just from the str(...) will create anything inside the brackets into a string data type.

#Num5
    #Again just like Num4, the str(34) changes anything that is inside the brackets to the string data type. Value is "34"

#Question 4

def main():
    print("   ___\n _|   |_ \n|       |\n|_______|\n  O   O")
    length = input("How many Kilometers did you drive: \n")
    length = length
    litres = input("How many litres did you use?\n")
    litres = litres
    print("you entered " + length + " km and " + litres + " litres")
    efficiency = (int(length)/int(litres))
    print("your car has an efficiency of " + str(efficiency) + " litres per kilometer")
    

main()

#This is supposed to be the answer but it's boring
'''
def main():
    print("   ___\n _|   |_ \n|       |\n|_______|\n  O   O")
    length = float(input("Km driven? "))
    litres = float(input("litres used? "))
    efficiency = length/litres
    print("your car has an efficiency of ", efficiency, " km/L")
main()
'''
#Question A.

'''
• Monthly interest rate can be calculated via annual interest divided by 12. 
• You must write main function and call it in your program
• Use format function to output only 2 digits after decimal point 
• Use comments in your program
• Follow the conventions to name your variables and constants
• The output should look like below, given the following inputs:
'''
def main():
    initial_sum = input("what is the iniial sum: ")
    initial_sum = int(initial_sum)
    monthlyInterestRate = input("annual interest rate: ")
    monthlyInterestRate = float((monthlyInterestRate))
    num_years = input("Input the number of years: ")
    num_years = int(num_years)
    future_capital = (float(initial_sum // monthlyInterestRate) * int(num_years) + initial_sum)
    future_capital = float(future_capital)
    print("Future capital is " + str(future_capital))
main()

#The correct answer is below
'''
def main():
 # getting input data
 intialSome = float(input("Enter the initial some: "))
 yIntRate = float(input("Enter annual interest rate: "))
 years = int(input(("Enter number of years: "))
 
 # calculate the capital 
 mIntRate = yIntRate / 12 / 100
 capital = initialSome * (1+ mIntRate) ** (years * 12) 
 # print out the results
 print("Future capital is", format(capital, "10.2f"))
main()

'''

x = input("Enter a number")
x = float(x)
y = input("Enter another number")
y = int(y)

print(format(x, '10.2f'))
print(format(y, '20'))
print(format(x + y, '20.2f'))

