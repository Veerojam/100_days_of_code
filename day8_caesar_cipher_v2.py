

# TODO-2.1: Create a function called decrypt() that decodes the original text.

# TODO-2.2: Combine the encrypt() and decrypt() functions into a single function called caesar().
# Use the value of the user chosen 'direction' variable to determine which functionality to use.
# Call the caesar function instead of encrypt, decrypt and pass in all three variables direction/ text/ shift


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = input("Type the shift number:\n")

# -------------- V2 ---------------

def caesar(direction, text, shift):
    
    new_text = ""

    if direction == "decode":
        shift *= -1
    
    for letter in text:
    
        new_location = (alphabet.index(letter) + shift) % len(alphabet)
        new_letter = alphabet[new_location]
        new_text += new_letter

    print(f"The {direction}d result is: {new_text}")

caesar("encode", "hello", 1)




# -------- V1 ----------------------
# def caesar(direction, text, shift):
      
#     if direction == "encode":
            
#         encoded_text = ""

#         for letter in text:

#             new_location = (alphabet.index(letter) + shift) % 26
#             new_letter = alphabet[new_location]
#             encoded_text += new_letter

#         print(f"The encoded text is: {encoded_text}")

#     else:

#         decoded_text = ""

#         for letter in text:

#             old_location = (alphabet.index(letter) - shift) % 26
#             old_letter = alphabet[old_location]
#             decoded_text += old_letter

#         print(f"The decoded text is: {decoded_text}")

# caesar("decode", "ifmmp", 1)


