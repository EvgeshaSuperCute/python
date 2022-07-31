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
    return coord

def distance(Point_1, Point_2):


    dist = ((Point_2[0]-Point_1[0])**(2) + (Point_2[1]-Point_1[1])**(2))**(0.5)
    return dist

#------------------------Main part---------------------------

print("Enter coordinates of point 1: ")
point_1 = checkInputValue()
print("Enter coordinates of point 2: ")
point_2 = checkInputValue()

print("Distance between point_1:", point_1, "and point_2", point_2," : ", distance(point_1, point_2))

