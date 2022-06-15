min = 100000000000000 
max = 0
while True:
    x = input("Enter a number: ")
    if x == "done":
        break
    try:
        num1 = float(x)
    except:
        print("Invalid input")
        continue
    if min > num1:
        min = num1
    if max < num1:
        max = num1
print("Maximum number = ", max)
print("Minimum number = ", min)


