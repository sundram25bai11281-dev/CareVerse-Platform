# Simple Calculator Program in Python

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero error."""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator_main():
    """Main function to run the calculator interface."""
    print("Welcome to the Simple Python Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        # Get user input for choice
        choice = input("\nEnter choice (1/2/3/4/5): ")

        # Check if choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                # Get the numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            result = None

            if choice == '1':
                result = add(num1, num2)
                operation_symbol = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation_symbol = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation_symbol = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation_symbol = "/"

            # Print the result
            print(f"\n{num1} {operation_symbol} {num2} = {result}")

        # Handle exit condition
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Handle invalid input
        else:
            print("Invalid Input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator_main()