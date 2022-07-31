from random import randint

def checkInputValue():
    value = 0
    ch = False

    while not ch:
        try:
            number = int(input("num: "))
            value = number
            ch = True
        except ValueError:
            print("It is wrong value, expected a number...")

    return value

def checkRange(data, list):
    for i in range(len(data)):
        if (data[i]-1) > len(list):
            print("Out of range, there are impossible positions in the file....")
            return 0

    print("Result of multiplication:",mult(list, data))


def set_list(n):
    list = []
    for i in range(n):
        list.append(randint(-n,n))
    return list

def get_data():
    f_data = open("data.txt", 'r')
    safe_data = [line.strip() for line in f_data]
    l_data = []

    for i in range(len(safe_data)):
        try:
            tm = int(safe_data[i])
            l_data.append(tm)
        except ValueError:
            print("There are incorrect values in the file, expected only numbers...")
            return None

    f_data.close()
    return l_data


def mult(num, data):
    mult = 1
    for i in data:
        mult *= num[i-1]
    return mult

def main_func():
    data = get_data()
    list = set_list(checkInputValue())
    print("Positions:",data)
    print("Values:",list)
    checkRange(data, list)


#------------------------Main part---------------------------

main_func()





