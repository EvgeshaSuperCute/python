def checkInputValue():
    value = 0
    ch = False

    while not ch:
        try:
            number = float(input("num: "))
            value = str(number)
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value

def summOfNums(value)->int:
    summ = 0;
    for i in range(len(value)):
        if value[i].isdigit():
            print(int(value[i]))
            summ+= int(value[i])
    return summ

#------------------------Main part---------------------------

print("Sum of numbers: ",summOfNums(checkInputValue()))