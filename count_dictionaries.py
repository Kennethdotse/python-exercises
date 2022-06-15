x= "hippopotamus"
count= {}
for letter in x:
    if letter not in count:
        count[letter]=1
    else:
        count[letter]=+1
print(count)
        
