def caesar(text, shift, direction):
    if direction == 'encode':
        cipher_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"The encoded text is {cipher_text}")
    elif direction == 'decode':
        decrypt_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift
                decrypt_text += alphabet[new_position]
            else:
                decrypt_text += char
        print(f"The decoded text is {decrypt_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_crypt = True
while end_crypt:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("wrong command")

    ask = input("do you want to run again?:").lower()
    if ask == 'yes':
        end_crypt = True
    elif ask == 'no':
        end_crypt = False
    else:
        print("wrong input")
        end_crypt = False