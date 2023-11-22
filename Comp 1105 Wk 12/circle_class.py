import shape

'''
def main():
    c1 = shape.Circle()
        #the statement above uses default values
    print(c1.rad, c1.color, c1.getArea())

    c2 = shape.Circle(-10, 'blue')
        #The statement above passes the values of 10 and blue to be 'rad', and 'color'
    print(c2.rad, c2.color, c2.getArea())
    
    c3 = shape.Circle(10)
        #uses the value of 10 for radius but uses default value of "white" for color. 
    print(c3.rad, c3.color, c3.getArea())
main()
'''


def square():
    s1 = shape.Square()
    print(s1.__cord_x, s1.__cord_y, s1.getSide(), s1.Area())

    s2 = shape.Square(8, 2, 10.0)
    print(s2.__cord_x, s2.__cord_y, s2.getSide(), s2.Area())

    s3 = shape.Square(1, 1)
    print(s3.__cord_x, s3.__cord_y, s3.getSide(), s3.Area())
square()