class Circle:
    #What type of data fields do you want in your class?
    #What if the class was a dog?
        #def __init__(self, breed, age, weight)
    def __init__(self, rad = 1, color = 'purple'):
            self.color = color
            self.rad = rad


    def getArea(self):
        area = ((self.rad^2) * 3.14)
        return area
    

class Square:

    def __init__(self, cord_x = 0, cord_y = 0, side = 1.0):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.side = side

    def valueX(self):
        locationX = self.cord_x
        return locationX
    
    def valueY(self):
        locationY = self.cord_y
        return locationY
    
    def getSide(self):
        side = self.side
        return side
    
    def Area(self):
        area = (self.side * self.side)
        return area