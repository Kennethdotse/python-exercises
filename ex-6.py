fname = input("Enter a filename: ")
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    count = count + 1
    print(line)
print(count)