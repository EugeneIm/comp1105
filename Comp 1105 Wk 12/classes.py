import random
#coin flip example

#Coin class has been created (all classes start uppercased)
class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup


def main():
    my_coin = Coin()
    print("The coin landed on:", my_coin.get_sideup())

main()