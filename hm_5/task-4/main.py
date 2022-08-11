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
    decode = ""
    for i in range(0, len(data), 2):
        for j in range(int(data[i])):
            decode += data[i+1]

    return decode


def main():
    op = input("For encode enter e, for decode enter d: ")
    if op == "d":
        t_data = input("Enter your string to decoding: ")
        m_decode = RLE_decode(t_data)
        print("Decoded string: ", m_decode)
    elif op == "e":
        t_data = input("Enter your string to encoding: ")
        m_encode = RLE_encode(t_data)
        print("Encoded string: ", m_encode)
    else:
        print("Unknown command...")


# ------------------------Main part---------------------------


if __name__ == "__main__":
    main()
