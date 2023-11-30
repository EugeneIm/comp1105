class Pet:
    def __init__(self):
        self.__name = "Noname"
        self.__animal_type = ""
        self.__age = 0

    def setName(self, newName):
        self.__name = newName


    def setType(self, newType):
        self.__animal_type = newType
    

    def setAge(self, newAge):
        self.__age = newAge
        

    def getName(self):
        return self.__name

    def getType(self):
        return self.__animal_type

    def getAge(self):
        return self.__age


def main():

    pet_one = Pet()
    x = input()
    y = int(input)
    z = input()
    pet_one.setName(x)
    pet_one.setAge(y)
    pet_one.setType(z)


main()