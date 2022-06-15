fname = input("Enter the filename: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence"):
        print(line)
        count = count + 1
        for x in line:
            x = float(line[20:])
            sum = x + sum
print(count)
print(sum)
print("Average = ",sum/count)
