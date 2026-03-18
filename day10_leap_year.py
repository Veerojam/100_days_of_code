


def is_leap_year(year):
    """Take a year and return output whether it's a leap year or not"""
    if year % 4 != 0:
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True 
        # if year % 100 == 0:
        #     print("False")
        # else:
        #     print("True")
    
    # and year % 400 == 0:
    #     if year % 100 == 0:
    #         return("Leap!")
    # else:
    #     return("Not Leap")


#is_leap_year(2000)

print(f"for 2000: {is_leap_year(2000)}, should be LEAP")
print(f"for 2100: {is_leap_year(2100)}, should be NOT LEAP")
print(f"for 2400: {is_leap_year(2400)}, should be TRUE")
print(f"for 1989: {is_leap_year(1989)}, should be FALSE")

# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder  

# e.g. The year 2000: 

#     2000 ÷ 4 = 500 (Leap)  
#     2000 ÷ 100 = 20 (Not Leap)  
#     2000 ÷ 400 = 5 (Leap!)  

# So the year 2000 is a leap year.  
