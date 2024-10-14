from uu import decode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caeser(original_text, shift_amount, direction):
    if shift_amount <= 0:
        print("Please enter a positive number!")
        return

    if direction == 'decode':
        shift_amount = -shift_amount
    elif direction == 'encode':
        ...
    else:
        print("Please type 'encode' to encrypt, type 'decode' to decrypt!")
        return

    encrypted_text = ""
    for char in original_text:
        if char not in alphabet:
            encrypted_text += char
            continue
        index = alphabet.index(char)
        shifted_index = index + shift_amount
        while shifted_index >= len(alphabet):
            shifted_index-=len(alphabet)
        while shifted_index < 0:
            shifted_index+=len(alphabet)
        encrypted_text += alphabet[shifted_index]
    return encrypted_text


print(caeser(text, shift,direction))




