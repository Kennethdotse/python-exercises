count = 0
fname = input("Enter a filename: ")
userinput = input("Enter a word: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    word = line.split()
    for  x in word:
        if x == userinput:
            count = count + 1
print (f"{fname} had {count} lines that matched {userinput}") 