from random import randint as rnd

def checkInputValue():
    value = 0
    ch = False
    i = 0
    while not ch:
        try:
            number = int(input())
            value = number
            ch = True
            i+=1
        except ValueError:
            print("It is wrong value, expected a number...")

    return value

def listFill():
    print("list size:", end="")
    n = checkInputValue()
    list = []
    for i in range(n):
        list.append(rnd(-99,99))
    print(list)
    return list

def summ(list):
    res = 0
    for i in range(1,len(list),2):
        res += list[i]
    return res

def main():
    list = listFill()
    print(summ(list))



#------------------------Main part---------------------------

if __name__ == "__main__":
    main()

