import datetime as d

def log(operation,data, result):
    f = open("logs.txt", "a")

    str_log = str(d.datetime.now()) + " | " + str(data[0])+" " + str(operation)+ " " + str(data[1]) + " = " + str(result) + "\n"
    f.write(str(str_log))


    f.close()


def s_e_log(step):
    f = open("logs.txt", "a")
    str_log = str(d.datetime.now())
    if step == 1:
        str_log+=  " | program start...\n"
    elif step == 0:
        str_log+=  " | program end...\n"

    f.write(str(str_log))

    f.close()