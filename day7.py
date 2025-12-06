# ---------------------------
# DAY 7: Revision + Practice (Function-Based)
# ---------------------------

# 1️⃣ Function to check even/odd for a single number
def check_even_odd(number):
    if number == 0:
        return "Number is zero"
    elif number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

def single_number_even_odd():
    num = int(input("Enter Any Number: "))
    print(check_even_odd(num))


# 2️⃣ Function to calculate sum, average, even/odd count, max/min for N numbers
def sum_average_even_odd_max_min():
    n = int(input("\nEnter how many numbers you want to sum: "))
    total = 0
    even = 0
    odd = 0
    max_num = None
    min_num = None

    for i in range(1, n+1):
        num = int(input(f"Enter number {i}: "))
        total += num

        # Max & Min check
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num

        # Even/Odd check
        if num % 2 == 0:
            print("Number is even")
            even += 1
        else:
            print("Number is odd")
            odd += 1

    print("\nThe sum of the numbers is:", total)
    print("Average:", round(total/n, 2))
    print("Even count:", even)
    print("Odd count:", odd)
    print("Maximum number:", max_num)
    print("Minimum number:", min_num)


# 3️⃣ Function for Simple Menu Calculator
def simple_calculator():
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1/2/3/4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid choice"

    print("Result:", result)


# ---------------------------
# Main program: Call all functions
# ---------------------------
if __name__ == "__main__":
    print("🎯 DAY 7: Revision + Practice")

    # Single number even/odd check
    single_number_even_odd()

    # Sum, average, even/odd count, max/min
    sum_average_even_odd_max_min()

    # Simple calculator
    simple_calculator()

    print("\n🎉 Congratulations! You have completed Day 7 practice successfully.")