student_scores = {
    "Harry": 80,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key]="A"
    elif student_scores[key]< 90 and student_scores[key]>=80:
        student_grades[key]="B"
    elif student_scores[key]>=60 and student_scores[key]<80:
        student_grades[key] = "C"
    elif student_scores[key] < 60:
        student_grades[key] = "Fail"

print(student_grades)