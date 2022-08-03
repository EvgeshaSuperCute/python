def checkInputValue():
    #value = 0
    ch = False
    list = []

    while not ch:
        try:
            number = int(input("num: "))
            list.append(number)
            #value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return list


