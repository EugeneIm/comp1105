def Task(p1, p2):
    sum = 0
    for x in range(p1, p2 + 1):
        sum += x
    print("between", p1, " and ", p2, "the sum is: ", sum)


#the function above has been put into a function to be read more easily and to repeat the same function multiple times with different parameters
def main():

    Task(12, 33)
    Task(56, 77)
    Task(1, 99)

main()