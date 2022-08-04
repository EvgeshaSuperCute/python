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
            i += 1
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def listFill():
    print("list size:", end="")
    n = checkInputValue()
    m_list = []
    for i in range(n):
        m_list.append(rnd(-9, 9))
    print(m_list)
    return m_list


def mult(p_list):
    res = []
    n = len(p_list)
    size = n//2 if n % 2 == 0 else n//2+1
    # print(n, "------------")
    for i in range(size):
        print(p_list[i], " : ", p_list[n - 1 - i])
        res.append(p_list[i] * p_list[n - 1 - i])

    return res


def main():
    t_list = listFill()
    print(mult(t_list))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
