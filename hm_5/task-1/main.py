count = {'Start': 0, 'End': 0}


def set_data(n):
    data = ""
    with open(f'text-{n}.txt', "r", encoding="utf-8") as f:
        data = f.read()
    return data


def findWords(data):
    f_str = input("|Enter text to find: \033[0m")
    i = 0
    tmp = list(data.split(" "))

    size = count["Start"] = len(tmp)


    while i != size:
        if tmp[i].find(f_str) != -1:
            tmp.pop(i)
            size -= 1
            i -= 1

        i += 1

    count["End"] = size
    return tmp


def textLayout(tmp_text) -> str:
    text = ""
    for i in tmp_text:
        text += i + " "
    return text


def main():
    out = findWords(set_data(input("\033[33m|Enter num of file: ")))
    m_text = textLayout(out)
    difference = count["Start"] - count["End"]
    print(m_text, f"\n\n\033[31m Count of deleted words: {difference}")

# ------------------------Main part---------------------------


if __name__ == "__main__":
    main()
