def sumNum(input):
    sum = 0
    #we start at 0 again

    while input > 0:
        amount = input % 10
        sum += amount
        input //= 10

    print(sum)
answer = sumNum(312)
print(answer)