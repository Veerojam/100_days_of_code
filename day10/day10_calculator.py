
ascii = '''
__________
| ________ |
||12345678||            _            _       _             
|""""""""""|           | |          | |     | |            
|[M|#|C][-]|   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
|[7|8|9][+]|  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
|[4|5|6][x]| | (_| (_| | | (__| |_| | | (_| | || (_) | |   
|[1|2|3][%]|  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
|[.|O|:][=]|
"----------"
'''

print(ascii)

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2
    
def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


to_continue = True
n1 = ""

while to_continue:

    if n1 == "":
        n1 = float(input("Please choose your first number: "))
        
    choice = input(f"+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("Please choose your second number: "))

    result = operations[choice](n1, n2)
    print(f"\n{n1} {choice} {n2} = {result}")

    choice_continue = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if choice_continue == "n":
        n1 = ""
        continue
    else: #start from picking an operation
        n1 = result
        continue


# ------------ Functionality --------------
# Programs asks the user to type the first number. - DONE
# Program asks the user to type a mathematical operator. - DONE
# Program asks the user to type a second number. - DONE
# Program works out the result based on the chosen mathematical operator. - DONE
# Program asks if the user wants to continue working with the previous result. 
    # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    # If no, program asks the user for the first number again and wipes all memory of previous calculations.