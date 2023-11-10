import random
#Lab Quiz 9 programming answer
def getData():
    n = int(input("Give me a number between 0 and 100: "))
    while n < 0:
        n = int(input("Number cannot be negative"))
    return n
def randNum():
    return random.randint(1, 1000)

def getKey():
    
    choice = random.randint(0,1)
    if choice == 0:
        key = chr(random.randint(ord('a'), ord('z')))
    else:
        key = chr(random.randint(ord('A'), ord('Z')))

    return key

def ranItem():
    return(getKey(), randNum())

def main():
    num = getData()
    d = {}
    for n in range(num):
        k, v = ranItem()
        while k in d:
            k, v = ranItem()
        d[k] = v
    print(d)

main()