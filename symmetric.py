def issymmetric(string):
    new_str = string[:3]
    length = len(string)
    string = string[3:]
    return new_str== string
check1 = issymmetric("kennet")
print(check1)
check2 = issymmetric("pappap")
print(check2)
