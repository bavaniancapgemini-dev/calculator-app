from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulus
from history import save_history
from utils import title
from percentage import percentage
from scientific import sine, cosine, tangent, logarithm
from history import show_history
from database import save_to_database
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
    print("14. Exit")

    choice = input("Choose operation: ")

    if choice == "14":
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
        print("Answer:", subtract(num1, num2))

        save_to_database(
        str(num1) + " - " + str(num2) + " = " + str(answer)
    )

    elif choice == "3":
        print("Answer:", multiply(num1, num2))

        save_to_database(
        str(num1) + " * " + str(num2) + " = " + str(answer)
    )

    elif choice == "4":
        print("Answer:", divide(num1, num2))

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

    else:
        print("Invalid Choice")