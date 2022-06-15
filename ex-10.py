maillog = {}
fname = input("Enter a filename: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        line = line.rstrip()
        line = line.split()
        for word in line:
            word = line[1]
            maillog[word] = maillog.get(word,0) + 1
print(maillog)
bigword = None
bigcount = None
for words,counts in maillog.items():
    if bigcount is None or counts > bigcount :
        bigcount = counts
        bigword = words
print(bigword,bigcount)


            

