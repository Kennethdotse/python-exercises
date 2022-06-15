try:
    fname = input("Enter a filename: ")
    fhand = open(fname)
except:
        if fname == "na na boo boo":
            print("NA NA BOO BOO TO YOU - you've been punk'd")
            quit()
        else:
            print(f"No such file or directory: {fname}")
            exit()
count = 0
a = 0
sum = 0
for line in fhand:
    if line.startswith("Received"):
        a = a + 1
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
print(f"There are {a} subject lines in the file")
