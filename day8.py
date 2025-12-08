# List of students
students = ["Mueen", "Abdullah", "Kinni", "Jake", "Alex"]

# Function to return PASS or FAIL
def check_result(marks):
    if marks >= 40:
        return "PASS"
    else:
        return "FAIL"

# Loop for each student
for student in students:
    print("Student:", student)
    marks = int(input("Enter marks: "))
    result = check_result(marks)
    print("Result:", result)
    print()