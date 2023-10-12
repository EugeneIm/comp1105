#un-finished while loop, finished one is on my home PC

BALANCE = int(input("Give me a starting balance: "))
RATE = 0.05
TARGET = (BALANCE * 2)
year = 0


while BALANCE < TARGET:
    year = year + 1
    INTEREST = BALANCE * RATE
    BALANCE = BALANCE + INTEREST
    if BALANCE < TARGET:
        print('not there yet')
        print("it is the year:", year)
        print(format(BALANCE, ".2f"))
    else:
        print('youve reached the target balance')