for i in range(1, 7):
    print(f"\n--- Student {i} ---")

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    result = "PASS" if marks >= 40 else "FAIL"

    print("Name:", name)
    print("Marks:", marks)
    print("Result:", result)
    