def checkInputValue():
    value = 0
    ch = False
    while not ch:
        try:
            number = int(input("Count of fibonacci numbers: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value


def fibNums(n):
    l_fib = []
    for i in range(n*2+1):
        l_fib.append(None)

    l_fib[n] = 0
    l_fib[n-1] = -1
    l_fib[n+1] = 1

    for i in range(2,n+1):
        l_fib[n - i] = l_fib[n-i+1]+l_fib[n-i+2]
        l_fib[n + i] = l_fib[n+i-1]+l_fib[n+i-2]

    return l_fib


def main():
    print("Fibonacci numbers: ", fibNums(checkInputValue()))


# ------------------------Main part---------------------------

if __name__ == "__main__":
    main()
