try:
    x = float(input("Enter Hours: "))
    y = float(input("Enter Rate: "))
except:
    print(f"Please enter a numeric input")
    exit()
if x > 40:
    z = 1.5*x*y
else:
    z = x*y
print("Pay= ", z )
