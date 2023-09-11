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

#Question 6

