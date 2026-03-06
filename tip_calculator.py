

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
nr_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * (tip / 100))
pay_per_person =  bill_with_tip / nr_of_people


final_result = print(f"Each person should pay: ${round(pay_per_person, 2)}")
