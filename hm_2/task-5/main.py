from random import randint


def l_suffle(list):
    for i in range(len(list)):
        idx = randint(0,len(list)-1)
        safe = list[idx]
        list[idx] = list[i]
        list[i] = safe
    return list


#------------------------Main part---------------------------

list = [1,2,3,4,5,6,7,8,9]


print("Before shuffle:",list)
print("After  shuffle:",l_suffle(list))

