def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    print("Welcome to the Command-Line Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        try:
            user_input = input("\nEnter your calculation (e.g., 2 + 3) or 'exit': ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye! Thanks for using the calculator.")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Please enter in the format: number operator number (e.g., 2 + 3)")
            
            num1_str, op, num2_str = parts
            
            num1 = float(num1_str)
            num2 = float(num2_str)
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                raise ValueError(f"Invalid operator '{op}'. Please use +, -, *, or /.")
            
            print(f"\nResult: {num1} {op} {num2} = {result:.2f}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()
