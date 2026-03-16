

#TODO-1.1: Create a function called 'encrypt()' that takes 'original_text' and 'shit_amount' as 2 inputs.
#TODO-1.2: Inside the 'encrypt' function, shift each letter of the original_text towards in the alphabet by the shift_amount and print the encrypted text.
# You can use the built-in Python index() to find out the position of an item in a list. e.g.
# fruits = ["Apple", "Pear", "Orange"]
# fruits.index("Pear")   = 1
# If we have the following values: plain_text = "hello" and shift_amount = 1, the final encrypted output should be: "Here is the encoded result: ifmmp"
#TODO-1.3: What happens if you try to shift z forwards by 9? Can you fix the code?
#TODO-1.4: Call the encrypt() function and pass in the user inputs. You should be able to encrypt the message.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = input("Type the shift number:\n")


def encrypt(original_text, shift_amount):

    new_text = ""

    for letter in original_text:
            
            new_location = (alphabet.index(letter) + shift_amount) % 26
            new_letter = alphabet[new_location]
            new_text += new_letter

    print(new_text)

encrypt("z", 2)
