count = {'Start': 0, 'End': 0}


def set_data(n):
    data = ""
    with open(f'text-{n}.txt', "r", encoding="utf-8") as f:
        data = f.read()
    return data


def checkWord(word, p_str):
    if word.find(p_str) != -1:
        return True
    else:
        return False


def findWords(data):
    f_str = input("|Enter text to find: \033[0m")
    i = 0
    tmp = list(data.split(" "))

    size = count["Start"] = len(tmp)

    while i != size:
        if checkWord(tmp[i], f_str):
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
