from degree_indexes import indexes



def getData(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readline()

def setPolynomial(n, polySumm):
    polynomial = ""
    val = 0
    for i in range(n, -1, -1):
        safe = val
        val = polySumm[i]
        if i > 1 and val > 0:
            polynomial += f"{val}x{to_deg(i)} + "
        elif i == 1 and val > 0:
            polynomial += f"{val}x"
        elif i > 1 and val == 0:
            polynomial += ""
        elif i == 1 and val == 0:
            polynomial += ""
        elif i == 0 and val > 0:
            if safe > 0:
                polynomial += f" + {val} = 0"
            elif safe == 0:
                polynomial += f"{val} = 0"
        elif i == 0 and val == 0:
            polynomial += " = 0"


    print(polynomial)
    return polynomial


def setData(polynomial):
    with open('polynomialSumm.txt', "+w", encoding="utf-8") as f:
        f.write(str(polynomial))
    return "________________________________\nCheck file polynomialSumm.txt"


def to_deg(DEG):
    degree = ""
    temp = str(DEG)
    for char in temp:
        degree += indexes[char] or ""

    return degree


def polynomialSumm(p_1, p_2):
    vals_1 = []
    vals_2 = []
    polySumm = []


    for i in range(len(p_1)):
        if p_1[i] == "=":
            break
        if p_1[i].isdigit() and p_1[i - 1] != "x":
            vals_1.append(int(p_1[i]))

    for i in range(len(p_2)):
        if p_2[i] == "=":
            break
        if p_2[i].isdigit() and p_2[i - 1] != "x":
            vals_2.append(int(p_2[i]))

    print(vals_1)
    print(vals_2)

    n = len(vals_1)

    for i in range(n):
        polySumm.append(vals_1[i] + vals_2[i])

    return list(reversed(polySumm))


def main():
    m_path = ['polynomial_1.txt', 'polynomial_2.txt']
    pln_1, pln_2 = getData(m_path[0]), getData(m_path[1])



    print(getData(m_path[0]))
    print(getData(m_path[1]))
    res = polynomialSumm(pln_1, pln_2)
    print(res)
    print(setData(setPolynomial(4, res)))
# ------------------------Main part---------------------------


if __name__ == "__main__":
    main()

