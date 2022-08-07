def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input("Num in decimal system: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def toBinary(value) -> str:
    l_bin = ""

    while value > 0:
        l_bin = str(value % 2) + l_bin
        value //= 2

    return l_bin


def main():
    print("Binary form: ", toBinary(checkInputValue()))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
