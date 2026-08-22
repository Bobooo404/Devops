def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a / b


while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Goodbye")
        break

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer:", add(a, b))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer:", subtract(a, b))

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer:", multiply(a, b))

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        answer = divide(a, b)

        if answer is not None:
            print("Answer:", answer)

    else:
        print("Invalid choice")