import operations.plus
import ui

def checkInputValue():
    value = 0
    ch = False

    while not ch:
        try:
            number = float(input("num: "))
            value = number
            ch = Tru
        except ValueError:
            print("It is wrong value, expected a number...")

    return value

def chsOperation(values):
    oper = input("Chose operation (+ - / *): ")
    res = None
    if oper == "+":
        res = operations.summ(values[0], values[1])
    elif oper == "-":
        res = operations.minus(values[0], values[1])
    elif oper == "/":
        res = operations.div(values[0], values[1])
    elif oper == "*":
        res = operations.mult(values[0], values[1])
    else:
        print("incorrect operation...")
    ui.fin(res)
    #print(values)
