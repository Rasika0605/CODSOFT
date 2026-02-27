# Moderate Level Calculator

def calculator():
    print("------ MODERATE CALCULATOR ------")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        print("\nChoose Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (x^y)")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == "5":
            print("Result =", num1 % num2)

        elif choice == "6":
            print("Result =", num1 ** num2)

        else:
            print("Invalid choice!")

        again = input("\nDo you want to calculate again? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for using the calculator!")
            break


calculator()