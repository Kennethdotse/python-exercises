try:
    x = int(input("enter a number: "))
#this is used to take all inputs of integers without taking strings

except:
    print(f"This is not a number!")
#this is used for exceptions of the data type

try:
    y = int(input("Enter a number: "))
except:
    print("This is not a number!")
    exit()
#this is used to stop the program when an integer is not entered
print(x+y)
#that ends it for today! THANK YOU!