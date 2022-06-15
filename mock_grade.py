sum = 0
while True:
    score = input("Enter the score : ")
    if score == "done":
        break
    try:
        x = int(score)
    except:
        print("Invalid input")
        continue
    sum = x + sum
print(sum)
def computegrade(score):
    if 79< score <=100:
        return(A)
    elif 69< score <= 79:
        return B
