import shape

def main():
    c1 = shape.Circle()
        #the statement above uses default values
    print(c1.radius, c1.color, c1.getArea())

    c2 = shape.Circle(10, 'blue')
        #The statement above passes the values of 10 and blue to be 'rad', and 'color'
    print(c2.radius, c2.color, c2.getArea())
    
    c3 = shape.Circle(10)
        #uses the value of 10 for radius but uses default value of "white" for color. 
    print(c3.radius, c3.color, c3.getArea())
main()



def square():
    s1 = shape.Square()
    print(s1.cord_x, s1.cord_y, s1.getSide())

    s2 = shape.Square(8, 2, 4.0)
    print(s2.cord_x, s2.cord_y, s2.getSide())

    s3 = shape.Square(1, 1)
    print(s3.cord_x, s3.cord_y, s3.getSide())
square()