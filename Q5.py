def decode(text, s):
    result = ""

    for char in text:
        if char == " ":
            result += char
            continue

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result

text = "Wkh vwdwxh lv exuulhg xqghu d wuhh pdunhg zlwk a rq Foxvwhu Lvodqg"
s = 3
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + decode(text, s))


