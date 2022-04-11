alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or 'decode to decrypt\n'")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def caesar(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == 'decode':
        shiftAmount *= -1
    for letter in startText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        endText += alphabet[newPosition]
    print(f"The {cipherDirection}d text is: {endText}")


caesar(startText=text, shiftAmount=shift, cipherDirection=direction)
