students = []
marks_list = []
results = []

for i in range(1,6):
     print(f"\nStudent {i}")

     name = input("Enter student name: ")
     marks = int(input("Enter marks: "))

     result = "PASS" if marks >= 40 else "FAIL"

     # Data store in lists
     students.append(name)
     marks_list.append(marks)
     results.append(result)

# Final Output
print("\n==== FINAL REPORT ====")
for i in range(5):
    print("\nStudent:",students[i])
    print("Marks:",marks_list[i])
    print("Result:",results[i])