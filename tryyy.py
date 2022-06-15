count = 0
sum = 0.0
small = 10000000000000000000000000000000000000
large = 0
while True:
    x = input("Enter a number: ")
    if x == "done":
        break
    try:
        num1 = float(x)
    except:
        print("Invalid Input")
        continue
    count = count +1
    sum = sum + num1
    if small > num1:
        small = num1
    if large < num1:
        large = num1
print("average = ", sum / count)
print("count= ", count)
print("sum= ", sum)
print("smallest number= ", small)
print("Largest number = ", large)
