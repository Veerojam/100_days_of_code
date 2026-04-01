
print("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
                                                              
""")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(direction, text, shift):
    
    new_text = ""
    correct_text = True
    if direction == "decode" or direction == "encode":

        if direction == "decode":
            shift *= -1
    
        for letter in text:
            if letter in alphabet:
        
                new_location = (alphabet.index(letter) + shift) % len(alphabet)
                new_letter = alphabet[new_location]
                new_text += new_letter

            else:
                # correct_text = False
                # break
                new_text += letter 
                
    # else:
    #     print("\nPlease provide the correct value of 'encode' or decode'.")
    #     return

    # if not correct_text:
    #     print("Please provide correct values!")
    
    print(f"The {direction}d result is: {new_text}\n")

start_again = True

while start_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(direction, text, shift)

    new_start = input("Do you want to continue? Yes or no? ").lower()

    if new_start == "no":
        start_again = False


# TODO-3.1: Import and print the logo art when the program starts. - DONE
# TODO-3.2: What happens if the user enters a number/symbol/space? - DONE
# TODO-3.3: Can you figure out a way to restart the cipher program? - DONE
