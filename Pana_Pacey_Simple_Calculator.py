
print("Simple Calculator")
print("MENU")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")

while True:
    operation = input("\nSelect Operation: ")

    if operation == "1":
        num_1 = int(input("Enter Number 1: "))
        num_2 = int(input("Enter Number 2: "))
        result = num_1 + num_2
        print("Addition result:", result)

    elif operation == "2":
        num_1 = int(input("Enter Number 1: "))
        num_2 = int(input("Enter Number 2: "))
        result = num_1 - num_2
        print("Subtraction result:", result)

    elif operation == "3":
        num_1 = int(input("Enter Number 1: "))
        num_2 = int(input("Enter Number 2: "))
        result = num_1 * num_2
        print("Multiplication result:", result)

    elif operation == "4":
        num_1 = int(input("Enter Number 1: "))
        num_2 = int(input("Enter Number 2: "))

        if num_2 != 0:
            print("Division result:", num_1 / num_2)
        else:
            print("Cannot divide by zero.")

    elif operation == "5":
        num_1 = int(input("Enter Number 1: "))
        num_2 = int(input("Enter Number 2: "))

        if num_2 != 0:
            print("Modulo result:", num_1 % num_2)
        else:
            print("Cannot get modulo by zero.")

    else:
        print("Invalid operation. Please select only 1-5.")
