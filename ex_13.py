time = {}
fname = input("Enter a filename: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        nline = line
        nnline = nline.rstrip()
        nnnline = nnline.split()
        if len(nnnline) <= 2:
            continue
        else:
            x = nnnline[5]
        for i in x:
            nx = x.split(":")
            nx = nx[0]
        time[nx] = time.get(nx,0) + 1
lst = list()
for (key,val) in time.items():
    tup = (key,val)
    lst.append(tup)
    new_lst = sorted(lst)
    #print(new_lst)
    for i in tup:
        a = tup[0]
        b = tup[1]
    print (f"{a} {b}")