import datetime as dt

def RLE_encode(data: str) -> str:
    data += "\0"
    count = 1
    encode = ""

    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            encode += str(count) + data[i]
            count = 1
    return encode


def RLE_decode(data: str) -> str:
    if len(data) < 2:
        print("Expected decoded string (1q2w3e...)")
        return "None"
    decode = ""
    for i in range(0, len(data), 2):
        for j in range(int(data[i])):
            decode += data[i+1]

    return decode


def getData(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readline()


def setData(data, typeOfResult: str):
    with open(f"{typeOfResult}#.txt", 'w') as f:
        return f.write(data)



def main():
    now = dt.datetime.now()
    op = input("For encode enter e, for decode enter d: ")

    if op == "d":
                                                 # t_data = getData("EncodedData-1.txt")
            t_data = input("Enter your string to decoding: ")
            tpr = f"EncodedData {now.day}-{now.month}-{now.year}#{now.hour}-{now.minute}-{now.second}"
            setData(t_data, tpr)
            m_decode = RLE_decode(t_data)
            print("Decoded string: ", m_decode)
            tpr = f"ResultOfDecodding {now.day}-{now.month}-{now.year}#{now.hour}-{now.minute}-{now.second}"
            setData(m_decode, "ResultOfDecodding")
    elif op == "e":
                                                 # t_data = getData("data-1.txt")
        t_data = input("Enter your string to encoding: ")
        tpr = f"DecodedData {now.day}-{now.month}-{now.year}#{now.hour}-{now.minute}-{now.second}"
        setData(t_data, tpr)
        m_encode = RLE_encode(t_data)
        print("Encoded string: ", m_encode)
        tpr = f"ResultOfEncodding {now.day}-{now.month}-{now.year}#{now.hour}-{now.minute}-{now.second}"
        setData(m_encode, tpr)
    else:
        print("Unknown command...")


# ------------------------Main part---------------------------


if __name__ == "__main__":
    main()
