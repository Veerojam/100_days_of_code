

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    number = student_scores[student]
    if number <= 70:
        number = "Fail"
        student_grades[student] = number
    elif 71 <= number <= 80:
        number = "Acceptable"
        student_grades[student] = number
    elif 81 <= number <= 90:
        number = "Exceeds Expectations"
        student_grades[student] = number
    else:
        number = "Outstanding"
        student_grades[student] = number

print(student_grades)



