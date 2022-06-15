lst1 = []
fname = input("Enter file name: ")
fhand= open(fname)
for line in fhand:
    lst = line.split()
    for word in lst:
        if word not in lst1:
            word=word.lower()
            lst1.append(word)
lst1.sort()
print(lst1)
