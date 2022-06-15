count = {}
fname = input("Enter a filename: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        line = line.rstrip()
        line = line.split()
        if len(line) <= 2:
            continue
        for word in line:
            word = line[2]
            count[word] = count.get(word,0) + 1
print(count)
bigword = None
bigcount = None
for words,counts in count.items():
    if bigcount is None or counts > bigcount :
        bigcount = counts
        bigword = words
print(bigword,bigcount)
            

