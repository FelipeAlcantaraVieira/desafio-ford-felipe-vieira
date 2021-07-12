# secret = "word"

def crypting(character):
    num = ord(character)
    if num < 65 or num > 90:
        return character
    if num >= 87:
        return chr(num - 22)
    return chr(ord(character) + 4)


def crypt():
    word = input("Qual palavra quer encriptar? ")
    upper_word = word.upper()
    crypted = "".join(map(crypting, list(upper_word)))
    print(crypted)
    return crypted


crypt()
