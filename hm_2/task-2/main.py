def checkInputValue():
    value = 0
    ch = False

    while not ch:
        try:
            number = int(input("num: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def multCollection(num):
    res = [];
    for i in range(num):
        res.append(i+1)
        for j in range(i):
            res[i]*=(j+1)

    return res
#------------------------Main part---------------------------

print(multCollection(checkInputValue()))