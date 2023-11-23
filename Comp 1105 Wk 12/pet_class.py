class Pet:
    def __init__(self, name, animal_type, age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

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

    pet_one = Pet("Sesame", "Dog", 1)
    pet_one.setAge(5)
    print(pet_one.getAge())
    pet_one.setName("marble")
    print(pet_one.getName())
    pet_one.setType('cat')
    print(pet_one.getType())


main()