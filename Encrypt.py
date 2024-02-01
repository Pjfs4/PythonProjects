alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
    new_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        if position + shift_number > len(alphabet):
            new_position = position + shift_number - 26
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_letter = alphabet[position + shift_number]
            new_text += new_letter
    print(f"The encoded text is {new_text}")


def decrypt(plain_text, shift_number):
    new_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        if position - shift_number < 0:
            new_position = position - shift_number + 26
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_letter = alphabet[position - shift_number]
            new_text += new_letter
    print(f"The decoded text is {new_text}")


if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
