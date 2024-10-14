alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        index = alphabet.index(char)
        shifted_index = index + shift
        if shifted_index >= len(alphabet):
            shifted_index-=len(alphabet)
        encrypted_text += alphabet[shifted_index]
    return encrypted_text


print(encrypt(text, shift))
