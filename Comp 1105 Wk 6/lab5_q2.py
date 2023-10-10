#function to receive a POSITIVE int as a PARAMETER and print the sum of the digits. 

def sumNum(input):
    sum = 0
    #we start at 0 again

    while input > 0:
        amount = input % 10
        sum += amount
        input //= 10

    print(sum)

sumNum(312)

