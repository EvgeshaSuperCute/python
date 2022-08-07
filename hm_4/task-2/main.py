import math


def primeFactors(num):
    res = []

    while num % 2 == 0:
        res.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            res.append(i)
            num = num / i
    if num > 2:
        res.append(int(num))
    return res


def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input("Enter the number: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def main():
    print(primeFactors(checkInputValue()))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
