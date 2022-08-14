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

    l_list = [rnd.randint(0, 9) for i in range(n)]

    print("Main elements:   ", l_list)
    return l_list




def getUniqueElements(p_list):

    resList = list(filter(lambda i: p_list.count(i) == 1, p_list))

    return resList


def main():
    m_list = listFill()
    print("Unique elements: ", getUniqueElements(m_list))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
