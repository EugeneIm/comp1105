#Function to accept an argument and display the argument multiplied by 10
def times_ten():
    v = getNum()
    u = getAnswer()
    t = getAnswer(u)

    print("number given was %d, answer is %.2f" % (v, t))

def getNum():
    value = int(input("Give me a number "))
    if value <= 0:
        value = int(input("value cannot be 0 or lower"))
    else:
        return value
    
def getAnswer(default = 1):
    answer = default * 10
    return answer
times_ten()


#header is def show_value(quantity), pass 12 as the argument


#def my_function(a, b, c)
#called as my_function(3, 2, 1)
#The value of a is 3, b is 2, c is 1, they correlate the order of variables to the order of values. 

def main():
    x = 1 
    y = 3.14
    print(x, y)
    #gives 1 3.14
    change_us(x, y)
    #gives 0 0 because change_us is using a, b and not x, y
    print(x, y)
    #1 3.14
def change_us(a, b):
    a = 0
    b = 0
    print(a, b)
    #1 3.14
    #change_us(x, y) changes the values of a and b to 1 and 3.14
main()