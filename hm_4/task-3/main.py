import random as rnd


def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input("list size: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def listFill():
    n = checkInputValue()
    l_list = []
    for i in range(n):
        l_list.append(rnd.randint(0, 9))

    print("Main elements:   ", l_list)
    return l_list


def getUniqueElements(list):
    checkSet = set()
    resList = []

    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                checkSet.add(list[i])
                break
    print()

    for i in list:
        ch = True
        for j in checkSet:
            if i == j:
                ch = False
        if ch:
            resList.append(i)

    return resList


def main():
    m_list = listFill()
    print("Unique elements: ", getUniqueElements(m_list))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
