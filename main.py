alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or 'decode to decrypt\n'")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(plainText, shiftAmount):
    cipherText = ""

    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"Your ecrypted message is: {cipherText}")


encrypt(plainText=text, shiftAmount=shift)
