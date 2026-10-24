
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


# Main calculator loop
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    next_calculation = input(
        "Do you want another calculation? (yes/no): "
    ).strip().lower()

    if next_calculation != 'yes':
        print("Calculator closed. Goodbye!")
        break
