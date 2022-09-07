import time
import random
import os

PlayerA = 'A'
PlayerB = 'B'
PlayerC = 'C'
PlayerD = 'D'

stepkey = 0
n = 0


# ------------Functions of partial formation of a list------------------/
# ------------of coordinates of moves for each player-------------------/


def form_step_q1(steps, step_key, n, A):
    for i in range(0, int(n / 2 + 1)):
        for j in range(int(n / 2 + 1), n):
            if A[i][j] == '*':
                # print(i,j,'|',A[i][j], end='  ', )
                steps[step_key][0] = int(i)
                steps[step_key][1] = int(j)
                step_key += 1
    return step_key


def form_step_q2(steps, step_key, n, A):
    for i in range(int(n / 2 + 1), n):
        for j in range(n - 1, int(n / 2 - 1), -1):
            if A[i][j] == '*':
                # print(i,j,'|',A[i][j], end='  ', )
                steps[step_key][0] = int(i)
                steps[step_key][1] = int(j)
                step_key += 1
    return step_key


def form_step_q3(steps, step_key, n, A):
    for i in range(n - 1, int(n / 2 - 1), -1):
        for j in range(int(n / 2 - 1), -1, -1):
            if A[i][j] =='*':
                # print(i,j,'|',A[i][j], end='  ', )
                steps[step_key][0] = int(i)
                steps[step_key][1] = int(j)
                step_key += 1
    return step_key


def form_step_q4(steps, step_key, n, A):
    for i in range(int(n / 2 - 1), -1, -1):
        for j in range(0, int(n / 2 + 1)):
            if A[i][j] == '*':
                steps[step_key][0] = int(i)
                steps[step_key][1] = int(j)
                step_key += 1
    return step_key

# ------------Formation of a list with the coordinates------------------/
# ------------of houses for each player---------------------------------/


def form_house_place(house, a, player_index):

    house_key = 0
    r_s = 0
    r_e = 0
    c_s = 0
    c_e = 0

    if player_index == 1:
        r_s = 1
        r_e = int(n / 2)
        c_s = int(n / 2)
        c_e = int(n / 2 + 1)
    elif player_index == 2:
        r_s = int(n / 2 +1)
        r_e = int(n - 1)
        c_s = int(n / 2)
        c_e = int(n / 2 + 1)
    # elif playerIndex == 3:
    #     r_s = 1
    #     r_e = int(n / 2)
    #     c_s = int(n / 2)
    #     c_e = int(n / 2 + 1)
    # elif playerIndex == 4:
    #     r_s = 1
    #     r_e = int(n / 2)
    #     c_s = int(n / 2)
    #     c_e = int(n / 2 + 1)

    for i in range(n):
        for j in range(n):
            if i in range(r_s, r_e) and j in range(c_s, c_e):
                if a[i][j] == 'D':
                    print(house_key)
                    house[house_key][0] = int(i)
                    house[house_key][1] = int(j)
                    house_key += 1

    if player_index == 2 or player_index == 4:
        house.reverse()


# ------------The function of forming a list with coordinates-----------/
# ------------for the moves of each player------------------------------/


def form_steps(steps, n, a, player_index): # PlayerIndex
    # PlayerIndex = 1
    if player_index == 1:
        form_step_q4(steps, form_step_q3(steps, form_step_q2(steps, form_step_q1(steps, stepkey, n, a), n, a), n, a), n, a)
    elif player_index == 3:
        form_step_q1(steps, form_step_q4(steps, form_step_q3(steps, form_step_q2(steps, stepkey, n, a), n, a), n, a), n, a)
    elif player_index == 2:
        form_step_q2(steps, form_step_q1(steps, form_step_q4(steps, form_step_q3(steps, stepkey, n, a), n, a), n, a), n, a)
    elif player_index == 4:
        form_step_q3(steps, form_step_q2(steps, form_step_q1(steps, form_step_q4(steps, stepkey, n, a), n, a), n, a), n, a)

# ----------------------------------------------------------------------/


def Play(stepsA, stepsB,A,n, PlayerA, PlayerB):

    sta = 0
    stb = 0
    ms = int(n * 4 - 4 + ((n-3)/2))
    A[stepsA[sta][0]][stepsA[sta][1]] = PlayerA
    A[stepsB[stb][0]][stepsB[stb][1]] = PlayerB

    # write, flush = sys.stdout.write, sys.stdout.flush

    # print(stepsA)
    os.system('cls')

    while sta <= ms or stb <= ms:

        # if simulateStep(A, stepsA, sta, ms, PlayerA) == 'break':
        #     break
        # else:
        #     sta += simulateStep(A, stepsA, sta, ms, PlayerA)
        #
        #
        # if simulateStep(A, stepsB, stb, ms, PlayerB) == 'break':
        #     break
        # else:
        #     stb += simulateStep(A, stepsA, sta, ms, PlayerA)
        A[stepsA[sta][0]][stepsA[sta][1]] = '*'
        A[stepsB[stb][0]][stepsB[stb][1]] = '*'
        bsta = sta
        bstb = stb
        ra = random.randint(1, 6)
        rb = random.randint(1, 6)
        sta += ra
        stb += rb

        if sta >= ms or stb >= ms:
            sta = sta - (sta - ms) - 1
            stb = stb - (stb - ms) - 1

        A[stepsA[sta][0]][stepsA[sta][1]] = PlayerA
        if sta in range(int(ms-((n-3)/2)), ms):
            A[stepsB[bstb][0]][stepsB[bstb][1]] = PlayerB
            print('player A rolled: ', ra)
            print('player B rolled: ', rb)
            printSimulateStep(PlayerA, PlayerB)
            print('Wins A')
            break

        A[stepsB[stb][0]][stepsB[stb][1]] = PlayerB
        if stb in range(int(ms-((n-3)/2)), ms):
            #A[stepsA[bsta][0]][stepsA[bsta][1]] = PlayerA
            print('player A rolled: ', ra)
            print('player B rolled: ', rb)
            printSimulateStep(PlayerA, PlayerB)
            print('Wins B')
            break

        print('player A rolled: ', ra)
        print('player B rolled: ', rb)
        printSimulateStep(PlayerA, PlayerB)


        #os.system('pause')

        time.sleep(0.5)
        os.system("cls")
    os.system('pause')
# ------------Simulation function of player moves-----------------------/


def printSimulateStep(Player_Active, Player_Passive):
    print('|'+('---'*n))
    for i in range(n):
        for j in range(n):
            if A[i][j] == Player_Active:
                print("\033[31m {}".format(A[i][j]), end=' ')
            else:

                if A[i][j] == Player_Passive:
                    print("\033[36m {}".format(A[i][j]), end=' ')
                elif A[i][j] == 'D':
                    print("\033[32m {}".format(A[i][j]), end=' ')
                else:
                    print("\033[0m {}".format(A[i][j]), end=' ')
        print()
    #os.system("pause")

#------------Create field function-------------------------------------/
def CreateMap(A, n):

    for i in range(n):
        for j in range(n):
            if i in range(int(n / 2 - 1), int(n / 2 + 2)) or j in range(int(n / 2 - 1), int(n / 2 + 2)):
                A[i][j] = '*'

    for i in range(n):
        for j in range(n):
            if i in range(int(n / 2), int(n / 2 + 1)) or j in range(int(n / 2), int(n / 2 + 1)):
                if (i != int(n / 2) or j != n - 1) and (i != n - 1 or j != int(n / 2)) and (i != int(n / 2) or j != 0) and (i != 0 or j != int(n / 2)):
                    A[i][j] = "D"

    A[int(n / 2)][int(n / 2)] = 'X'

# ------------Сontrol function of the input value of the field size-----/


def sizeControl():
    check = False
    n = None
    while check == False:
        n = input('Enter size of board (only odd number and more than 4): ')
        n = int(n)
        if n % 2 == 0 or n < 5:
            check = False
            print('Wrong size!')
            if n < 5:
                print('impossible options... ')
                print('Must be more then 5')
                print('Please enter another value')
            else:
                print('possible options: ', n - 1, 'or ', n + 1)
                print('Please enter another value or one of this')
            os.system('pause')
            os.system('cls')
        else:
            check = True
    return n


# ------------Start of program------------------------------------------/


n = sizeControl()
os.system('cls')


# -----------Allocating memory for dynamic lists-------/
stepsA = [0] *(n*4-4)
for i in range(n*4-4):
    stepsA[i] = [' '] * 2

stepsB = [0] *(n*4-4)
for i in range(n*4-4):
    stepsB[i] = [' '] * 2


houseA = [0] * (int(((n-3)/2)))
for i in range(int(((n-3)/2))):
    houseA[i] = [' '] * 2

houseB = [0] * (int(((n-3)/2)))
for i in range(+int(((n-3)/2))):
    houseB[i] = [' '] * 2

A = [''] * n
for i in range(n):
    A[i] = [' '] * n
# ----------------------------------------------------/

CreateMap(A, n)

form_house_place(houseA, A, 1)
form_house_place(houseB, A, 2)
form_steps(stepsA, n, A, 1)
form_steps(stepsB, n, A, 2)

stepsA += houseA
stepsB += houseB

A[stepsA[0][0]][stepsA[0][1]] = PlayerA
A[stepsB[0][0]][stepsB[0][1]] = PlayerB
os.system('cls')

printSimulateStep(PlayerA, PlayerB)
os.system('pause')

Play(stepsA, stepsB,A,n, PlayerA, PlayerB)
