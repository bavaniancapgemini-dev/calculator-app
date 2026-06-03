from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulus
from history import save_history
from utils import title
from percentage import percentage
from scientific import sine, cosine, tangent, logarithm
from history import show_history
from database import save_to_database
from database import view_database_history
from health import bmi
from age import calculate_age
from converter import *
from export import export_history

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


while True:

    title()

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Percentage")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Logarithm")
    print("13. Show History")
    print("14. Database History")
    print("15. BMI Calculator")
    print("16. Age Calculator")
    print("17. KM to Miles")
    print("18. Celsius to Fahrenheit")
    print("19. Export JSON")
    print("20. Exit")

    choice = input("Choose operation: ")

    if choice == "20":
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        answer = add(num1, num2)

        print("Answer:", answer)

        save_to_database(
        str(num1) + " + " + str(num2) + " = " + str(answer)
    )

        save_history(
    str(num1) + " + " + str(num2) + " = " + str(answer)
)

    elif choice == "2":

        answer = subtract(num1, num2)
        
        print("Answer:", answer)

        save_to_database(
        str(num1) + " - " + str(num2) + " = " + str(answer)
    )

    elif choice == "3":
        answer = multiply(num1, num2)
        print("Answer:", answer)

        save_to_database(
        str(num1) + " * " + str(num2) + " = " + str(answer)
    )

    elif choice == "4":
        answer = divide(num1, num2)
        print("Answer:", answer)

        save_to_database(
        str(num1) + " / " + str(num2) + " = " + str(answer)
    )

    elif choice == "5":
        print("Answer:", power(num1, num2))

    elif choice == "6":
        print("Answer:", square_root(num1))

    elif choice == "7":
        print("Answer:", modulus(num1, num2))

    elif choice == "8":

        total = int(input("Enter total number: "))
        percent = int(input("Enter percentage: "))

        answer = percentage(total, percent)

        print("Answer:", answer)

    elif choice == "9":

        number = int(input("Enter number: "))

        print("Answer:", sine(number))

    elif choice == "10":

        number = int(input("Enter number: "))

        print("Answer:", cosine(number))

    elif choice == "11":

        number = int(input("Enter number: "))

        print("Answer:", tangent(number))

    elif choice == "12":

        number = int(input("Enter number: "))

        print("Answer:", logarithm(number))

    elif choice == "13":

        show_history()

    elif choice == "14":
        records = view_database_history()

        for record in records:

            print(record)

    elif choice == "15":
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))
        print("BMI:", bmi(weight, height))

    elif choice == "16":
        year = int(input("Enter birth year: "))
        print("Age:", calculate_age(year))

    elif choice == "17":
        km = float(input("Enter distance in km: "))
        print("Distance in miles:", km_to_miles(km))

    elif choice == "18":
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

    elif choice == "19":
        export_history()
        print("History Exported to JSON")

    elif choice == "20":
        break
    else:
        print("Invalid Choice")