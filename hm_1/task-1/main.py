#TASK - 1

def checkDay(num):
    if 0 >= num or num > 7:
        print("it isn't a week's day :|")
    elif 6 <= num <= 7:
        print("it's weekend :(")
    elif 0 < num < 6:
        print("it's workday ;)")

def checkInputValue():
    day = input("Please enter your day: ")
    if str.isdigit(day):
        num = int(day)
        checkDay(num)
    else:
        print("It isn't a number")
        return 0
    return 1
#------------------------Main part---------------------------

ch = 1

while ch != 0:
    ch = checkInputValue()






