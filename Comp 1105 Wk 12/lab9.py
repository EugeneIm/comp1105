import shape
 
def main(): 
    s1 = shape.Square() 
    print('s1='+ s1.str()) 
 
    s2 = shape.Square(2, -1, 4) 
    print('s2='+ s2.str()) 
 
    print('s1 is left side of s2:', s2.isLeftside(s1))  
 
    s2.translateXY(-6, -1) 
    print('s2={x:', s2.valueX(),', y:', s2.valueY(), ', side:', s2.getSide(),'}', sep='') 
 
    print('s2 is left side of s1:', s1.isLeftside(s2))  
     
    s2.setSide(6.5) 
    print('s2='+ s2.str()) 
     
    print('s2 is left side of s1:', s1.isLeftside(s2))  
 
# call the main function 
main() 