


# def life_in_weeks(nr):
#     weeks = int((90 - nr) * 52)
#     print(f"You have {weeks} weeks left.")
    
# life_in_weeks(20)


# def greet_with(name, location):
#     print(f"Hello {name} from {location}")

# greet_with(name = "Tim", location = "London")

def calculate_love_score(name1, name2):

    true = "true"
    love = "love"
    names = str(name1 + name2)

    nr = 0
    nr2 = 0
    for letter in names:
        if letter in true:
            nr += 1
    for letter in names:
        if letter in love:
            nr2 += 1
    print(f"{nr}{nr2}")

calculate_love_score("Angela Yu", "Jack Bauer")