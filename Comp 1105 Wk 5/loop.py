#un-finished while loop, finished one is on my home PC

BALANCE = int(input("Give me a starting balance: "))
RATE = 0.05
TARGET = (BALANCE * 2)
year = 0


while BALANCE < TARGET:
    year = year + 1
    INTEREST = BALANCE * RATE
    NEW_BALANCE = BALANCE + INTEREST
    if NEW_BALANCE < TARGET:
        print('not there yet')
    else:
        print('youve reached the target')