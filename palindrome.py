def ispalindrome(string):
    new_str = ""
    for i in range (len(string)-1,-1,-1):
        new_str+= string[i]
        x = new_str
        print(x)
    return new_str==string
check= ispalindrome("nima")

print (check)