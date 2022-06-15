score = float(input("Enter score: "))
def computegrade(score):
    if 0.9<=score<=1.0 :
        return("A")
    elif 0.8<=score < 0.9:
        return("B")
    elif 0.7<=score < 0.8:
        return("C")
    elif 0.6 <=score<= 0.5:
        return("D")
    elif 0.4 <=score< 0.5:
        return( "E" )
    elif 0.0<=score<=0.4:
        return("F")
    else: 
        return("Bad score")
print(computegrade(score))

       
