#Function to receive a positive int as a paramter and calculates the sum of only the even and odd numbers. 

def sumNums(num):
    #again we start with a total that is set a 0 in the beginning. 
    #but this time we need two totals, one for even and one for odd.
    evenSum = 0
    oddSum = 0
    while num > 0:
        value = num % 10
        if value % 2 == 0:
            evenSum += value
        else:
            oddSum += value
        
        num //= 10

    print(" value of even numbers is", evenSum, "\n", "value of odd numbers is",  oddSum)
sumNums(9)
