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

def summ(num):
    res = 0;
    list = []

    for i in range(num):
        res += (1 + (1 / (i + 1))) ** (i + 1)
        list.append(res)
    return list


#------------------------Main part---------------------------

res_list = summ(checkInputValue())

for i in range(len(res_list)):
    print(i+1,":", res_list[i])
