
# Name: Pacey Ken Paña
# Section: 3418
# Activity: Laboratory Activity 4 - BMI Calculator

while True:

    
    print("================================")
    print("         BMI CALCULATOR")
    print("================================")
    print("1. Calculate BMI")
    print("2. View BMI Categories")
    print("3. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    
    if choice == "1":

        print()

        name = input("Enter your name: ")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        
        if weight <= 0 or height <= 0:
            print()
            print("Invalid input. Weight and height must be greater than zero.")

        else:
          
            bmi = weight / (height * height)

          
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            
            print()
            print("================================")
            print("           BMI RESULT")
            print("================================")
            print("Name:", name)
            print("Weight:", weight, "kg")
            print("Height:", height, "m")
            print(f"BMI: {bmi:.2f}")
            print("Category:", category)
            print("================================")

   
    elif choice == "2":

        print()
        print("BMI CATEGORIES")
        print("Below 18.5       : Underweight")
        print("18.5 to below 25 : Normal weight")
        print("25 to below 30   : Overweight")
        print("30 and above     : Obesity")
        print()

    
    elif choice == "3":

        print()
        print("Thank you for using the BMI Calculator!")
        break

   
    else:
        print()
        print("Invalid choice. Please select 1, 2, or 3.")

    print()
