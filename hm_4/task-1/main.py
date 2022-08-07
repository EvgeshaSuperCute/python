import math as m


def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = float(input("Enter the accuracy from 0.n to 0.0000000...n : "))
            if number < 0 or number > 1:
                ch = False
                print("It is wrong value, expected an accuracy from 0.n to 0.0000000...n ")
            else:
                ch = True

            value = number

        except ValueError:
            print("It is wrong value, expected an accuracy from 0.n to 0.0000000...n ")

    return value


def accuracy() -> int:
    j = 0
    l_acr = checkInputValue()
    step = 1
    while (step * l_acr) % 1 != 0:
        print(l_acr)
        step *= 10
        j += 1
    return j


def main():

    print("Pi number: ", '%.{acr}f'.format(acr=accuracy()) % float(m.pi))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
