fhand = open("knust-short.txt")
counts = dict()
for line in fhand:
    line = line.rstrip()
    if line. startswith("From "):
        elements = line.split()
        day = elements[1]
        counts[day]=counts.get(day,0)+1
print(counts)
highest = max(counts)
print(highest,counts[highest])