def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    fin = encrypt(text, 26 - s)

    return fin


text = input()
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Encrypt: " + encrypt(text, s))
temp = encrypt(text, s)
print("Decrypt: " + decrypt(temp, s))
