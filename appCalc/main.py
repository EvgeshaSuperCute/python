import tools as t
import logs as l

l.s_e_log(1)

values = []

for i in range(2):
    values.append(t.checkInputValue())

t.chsOperation(values)

l.s_e_log(0)





#values = []
# operation = []
#
# expression = input("Enter expression: ")
#
# for i in expression:
#     print(i)