def triangleArea(b,h):
    myArea = 0.5 *b * h
    return myArea
def trianglePerimeter(l,b):
    myPerimeter = 2*l + b
    return myPerimeter
Area= triangleArea(10,5)
Perimeter = trianglePerimeter(10,5)
print("Area ={} Perimeter={}".format(Area, Perimeter))
P = int(input("Enter the Principal: "))
R = int(input("Enter the Rate: "))
T = int(input("Enter the time: "))
def simpleInterest(P,R,T):
    myInterest = P*R*T/100
    return myInterest
interest = simpleInterest(P,R,T)
print(interest)
    

