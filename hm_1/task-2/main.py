def checkInputValue():
    predicates = ["x","y","z"]
    values = []
    ch = True
    negative = False
    for i in range(3):
        ch = False
        while ch == False:
            el = input("Enter " + predicates[i] +":")
            negative = False
            if el[0]== "-":
                el = el[1:]
                negative = True

            if el.isdigit():# and (el == '0' or el == '1'):           #-если только для 0 и 1
                ch = True
                if negative:
                    values.append(-int(el))
                else:
                    values.append(int(el))
            else:
                #print("It is wrong value, expected value 0 or 1...") #-если только для 0 и 1
                print("It is wrong value, expected a number...")
    logExpr(values)

def logExpr(values):
    answer = False
    Val_1 = not(values[0] or values[1] or values[2])
    Val_2 = (not values[0] and not values[1] and not values[2])

    answer = True if Val_2 == Val_1 else False

    print("The value of a logical expression:", answer)

#------------------------Main part---------------------------

checkInputValue()
