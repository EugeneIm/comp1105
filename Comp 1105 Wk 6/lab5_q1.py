#Q1
    #Function that receives a positive int and calculates the sum of all the numbers, i.e. if the int is 312, sum is 6, (3 + 1 + 2)

def sumNum():
    numInput = int(input("Give me a number "))
    #number has to be valid
    while numInput <= 0:
        print("Number can't be equal to or less than 0")
    
    #at the first loop the sum is at the value 0 since it hasn't added anything yet
    sum = 0
    while numInput > 0:
        #the variable "number" is given the value of the input modulus 10. i.e. if numInput = 312, modulus 10 gives you "2" 
        number = numInput % 10
        sum += number
        #a new variable called "sum" stores the value of the modulus

        numInput //= 10
        #after taking the "2" from 312, you divide it again leaving "31", and repeat until all the digits have been added together
    print(sum)

sumNum()


'''
print("Hello", "World", sep=' ', end='#')
    #this works fine
print("Hello", "World", end='#', sep=' ')
    #"end" and "sep" can be interchanged in order
print(end='#',"Hello", "World", sep=' ')
    #arguments cannot be put in after a keyword such as "end" or "sep"
print(end='#', sep=' ', "Hello", "World")
    #same as before, even if you put all the keywords in front of the arguments, same thing as before. 
'''