import string
def encryption(word):
    codeword = "cat"
    alph = string.ascii_lowercase
    dict = {char: index for index, char in enumerate(alph)}
    new_text = ""
    n = 0
    numbers = ""
    for i, j in enumerate(word):
        if not j.isalpha():
            if j.isnumeric():
                numbers += f"{i}{j}"
            else:
                new_text += j
            continue
        flag = False
        if n == len(codeword):
            n = 0
        codeletter = codeword[n]
        if codeletter.isupper():
            codeletter = codeletter.lower()
        if j.isupper():
            j = j.lower()
            flag = True
        c = chr((dict[j] + dict[codeletter]) % len(alph) + ord("a"))
        if flag:
            c = c.upper()
        new_text += c
        n += 1
    return new_text + numbers


def decryption(word):
    codeword = "cat"
    alph = string.ascii_lowercase
    dict = {char: index for index, char in enumerate(alph)}
    new_text = ""
    numbers = []
    n = 0
    l = 0
    for i in range(len(word)):
        if word[i].isnumeric():
            l += 1
            numbers.append(word[i])
    for i in range(len(word) - l):
        j = word[i]
        if not j.isalpha() or j == " ":
            new_text += j
            continue
        flag = False
        if n == len(codeword):
            n = 0
        codeletter = codeword[n]
        if codeletter.isupper():
            codeletter = codeletter.lower()
        if j.isupper():
            j = j.lower()
            flag = True
        c = chr((dict[j] - dict[codeletter]) % len(alph) + ord("a"))
        if flag:
            c = c.upper()
        new_text += c
        n += 1
    new_text = list(new_text)
    for i, j in enumerate(numbers):
        if i % 2 == 0:
            continue
        else:
            index = int(numbers[i - 1])
            if index >= len(new_text):
                new_text.append(j)
                continue
            text_move = new_text[index:]
            new_text = new_text[:index]
            new_text.append(j)
            new_text += text_move
    return "".join(new_text)
