maillog = {}
fname = input("Enter the filename: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        word = line
        word = word.rstrip()
        word = word.split()
        for item in word:
            item = word[1]
            maillog[item] = maillog.get(item,0) + 1
lst = list()
for email,counts in maillog.items():
    tup = (counts,email)
    lst.append(tup)
new_lst = sorted(lst, reverse=True )
x = (new_lst[0])
print (f"{x[1]} {x[0]}")





