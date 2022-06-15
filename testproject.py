test =[]
while True:
    num = input("Enter your score: ")
    if num == "done":
        break
    else:
        test.append(int(num))
print("maximum=", max(test))
print("minimum=", min(test))
print("average=", sum(test)/len(test))