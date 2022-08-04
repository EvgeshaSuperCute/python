import random as rnd


def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input())
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def printList(p_list):
    for i in range(len(p_list)):
        print('[%.3f]' % p_list[i], end=" ")
    print('\n')


def listFill():
    print("list size:", end="")
    n = checkInputValue()
    l_list = []
    for i in range(n):
        l_list.append(rnd.randint(-9, 9)+rnd.random())

    printList(l_list)
    return l_list


def maxFractPart(p_list) -> str:
    l_max = 0.0
    n = len(p_list)

    for i in range(n):
        safe_f_p = str(p_list[i]).split('.')
        if float('0.' + safe_f_p[1]) > l_max:
            l_max = float('0.' + safe_f_p[1])

    return str(l_max)


def main():
    m_list = listFill()
    print("Max fractional part: ", '%.3f' % float(maxFractPart(m_list)))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
