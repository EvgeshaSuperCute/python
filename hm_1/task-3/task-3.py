def checkInputValue():
    xy = ["x","y"]
    coord = [None, None]
    ch = True
    negative = False
    for i in range(2):
        ch = False
        while ch == False:
            el = input("Enter " + xy[i] +":")
            negative = False
            if el[0]== "-":
                el = el[1:]
                negative = True

            if el.isdigit():
                ch = True
                if negative:
                    coord[i]=(-int(el))
                else:
                    coord[i]=(int(el))
            else:
                print("It is wrong value, expected a number...")

            if coord[0] == 0 == coord[1]:
                print("--- THE ORIGIN POINT ---")
                print(" Try another coordinates")
                ch = False

    checkQuarter(coord)


def checkQuarter(coord):

    print("(x,y): ", coord)
    x = coord[0]
    y = coord[1]

    if x == 0:
        print("a point on the x-axis")
        return
    elif y == 0:
        print("a point on the y-axis")
        return

    quarter = 0
    if x > 0 and y > 0:
        quarter = 1
    elif x < 0 and y < 0:
        quarter = 3
    elif x > 0 and y < 0:
        quarter = 4
    elif x < 0 and y > 0:
        quarter = 2

    print("The point in the " + str(quarter) + " quarter")

#------------------------Main part---------------------------

checkInputValue()