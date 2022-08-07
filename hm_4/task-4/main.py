import random as rnd
import degree_indexes as di


def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input("Enter the degree of the polynomial: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def setPolynomial(n):
    polynomial = ""
    val = 0
    for i in range(n, -1, -1):
        safe = val
        val = rnd.randint(0, 5)
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
    with open('polynomial.txt', "+w", encoding="utf-8") as f:
        f.write(str(polynomial))

def to_deg(DEG):
    degree = ""
    temp = str(DEG)
    for char in temp:
        degree += di.indexes[char] or ""

    return degree



def main():
    setData(setPolynomial(checkInputValue()))

# ------------------------Main part---------------------------


if __name__ == "__main__":
    main()
