student_marks = {"Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 75}
student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"The student marks for {student_name} are: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")