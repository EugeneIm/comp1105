def Task(p1, p2):
    sum = 0
    for x in range(p1, p2 + 1):
        sum += x
    print("between", p1, " and ", p2, "the sum is: ", sum)


def main():
    
    Task(12, 33)
    Task(56, 77)
    Task(1, 99)

main()