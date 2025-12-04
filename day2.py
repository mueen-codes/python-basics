name = input("What is your name? ")
marks = int(input("What are your Physics marks? "))

if marks >= 80:
    grade = "A+"
    result = "PASS"
elif marks >= 70:
    grade = "A"
    result = "PASS"
elif marks >= 60:
    grade = "B"
    result = "PASS"
elif marks >= 50:
    grade = "C"
    result = "PASS"
elif marks >= 40:
    grade = "D"
    result = "PASS"
else:
    grade = "F"
    result = "FAIL"

print("\n--- Student Result ---")
print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Result:", result)