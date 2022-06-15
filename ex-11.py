maillog = {}
fname = input("Enter a filename: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        line = line.rstrip()
        line = line.split("@")
        for word in line:
            x = word
            x = x.split()
            if len(x) == 2 :
                continue
            for item in x:
                item = x[0]
                maillog[item] = maillog.get(item,0) + 1
print(maillog)
bigword = None
bigcount = None
for words,counts in maillog.items():
    if bigcount is None or counts > bigcount :
        bigcount = counts
        bigword = words
print(f"{bigword} sent {bigcount} mails")


            

