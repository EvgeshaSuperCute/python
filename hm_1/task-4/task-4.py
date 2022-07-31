def checkInputValue():
    quarter = input("Please enter your Quater: ")
    if str.isdigit(quarter):
        num = int(quarter)
        if num > 4 or num < 1:
            print("Expected 1..4, try again: ")
            return 1
        checkQuarter(num)
    else:
        print("It isn't a number")
        return 0
    return 1

def checkQuarter(quarter):
    if quarter == 1:
        print("X ∈ (0;∞+) and Y ∈ (0;∞+)")
    elif quarter == 2:
        print("X ∈ (0;∞-) and Y ∈ (0;∞+)")
    elif quarter == 3:
        print("X ∈ (0;∞-) and Y ∈ (0;∞-)")
    elif quarter == 4:
        print("X ∈ (0;∞+) and Y ∈ (0;∞-)")


#------------------------Main part---------------------------

ch = 1

while ch != 0:
    ch = checkInputValue()

