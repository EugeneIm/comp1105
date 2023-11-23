class Circle:
    def __init__(self, radius=1, theColor='White'):
        if radius > 0:
            self.r = radius
            self.__color = theColor
        else:
            return None

    def area(self):
        result = self.r * self.r * 3.14
        return result

    def getColor(self):
        return self.__color

    def setColor(self, newColor):

        self.__color = newColor


def main():
    c1 = Circle(10, 'Red')
    print(c1.r, c1.getColor(), c1.area())

    c1.setColor("White")
    print(c1.r, c1.getColor(), c1.area())


main()
