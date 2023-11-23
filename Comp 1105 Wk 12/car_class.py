class Car:
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        #adds 5 to the speed every time it's called
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
        #subtract 5 every time
    def get_speed(self):
        #return current speed 
        return self.__speed

    def get_YearModel(self):
        return self.__year_model
    
    def getMake(self):
        return self.__make
    
    def setSpeed(self, newValue):
        #newValue is a parameter that has to be passed through so that the program uses that value and replaces the previous value. 
        self.__speed = newValue



def main():

    car_one = Car(2020, "audi")
    for i in range(5):
        car_one.accelerate()
    print(car_one.get_speed())
    for i in range(5):
        car_one.brake()
        print(car_one.get_speed())
    print(car_one.get_YearModel())
    print(car_one.getMake())
    car_one.setSpeed(80)
    print(car_one.get_speed())

main()