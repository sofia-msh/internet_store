def cypher(text,code_word):
    base_low = ord("a")
    base_up = ord("A")
    new_text = []
    n = 0
    code_letter = code_word[n]
    for j in text:
        if j.isupper():
            new_text.append(chr((ord(j) + ord(code_letter)) % (ord("Z") - ord("A")) + base_up))
            n += 1
        elif j.islower():
            new_text.append(chr((ord(j) + ord(code_letter)) % (ord("z") - ord("a")) + base_low))
            n += 1
        else:
            new_text.append(chr((ord(j) + ord(code_letter))))
            n += 1
        if n > len(code_word)-1:
            n = n % (len(code_word)-1)
    return "".join(new_text)


print(cypher("abc", "xyz"))