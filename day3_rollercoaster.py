print("Welcome to the rollercoaster")
height = int(input("what's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12:
        #print("Please pay $5.")
        bill += 5
    elif age <= 18:
        #"Please pay $7."
        bill += 7
    else:
        #"Please pay $12."
        bill += 12
    photo = input("Do you want a photo taken? Please answer yes or no: ")
    if photo == "yes":
        bill += 3
        print(f"Your total bill is {bill}$")
    
    print(f"Your total bill is {bill}$")
else:
    print("Sorry, you have to grow taller before you can ride diz ride")