def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def miles_to_kilometers(m):
    return m * 1.60934

def kilometers_to_miles(k):
    return k / 1.60934

def pounds_to_kilograms(p):
    return p * 0.453592

def kilograms_to_pounds(k):
    return k / 0.453592

# Dictionary of conversion functions
conversions = {
    'temperature': {
        'Celsius to Fahrenheit': celsius_to_fahrenheit,
        'Fahrenheit to Celsius': fahrenheit_to_celsius
    },
    'distance': {
        'Miles to Kilometers': miles_to_kilometers,
        'Kilometers to Miles': kilometers_to_miles
    },
    'weight': {
        'Pounds to Kilograms': pounds_to_kilograms,
        'Kilograms to Pounds': kilograms_to_pounds
    }
}

def display_menu(category):
    print(f"\nAvailable {category} conversions:")
    options = list(conversions[category].keys())
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print(f"{len(options)+1}. Back to main menu")
    return options

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Unit Converter Program")
    
    while True:
        print("\nMain Menu:")
        print("1. Temperature Conversions")
        print("2. Distance Conversions")
        print("3. Weight Conversions")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                category = 'temperature'
            elif choice == 2:
                category = 'distance'
            elif choice == 3:
                category = 'weight'
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
                continue
                
            options = display_menu(category)
            conv_choice = int(input("Enter conversion choice: "))
            
            if conv_choice == len(options)+1:
                continue
            elif 1 <= conv_choice <= len(options):
                selected_conversion = options[conv_choice-1]
                value = get_float_input(f"Enter value to convert: ")
                result = conversions[category][selected_conversion](value)
                
                # Extract units for display
                from_unit, to_unit = selected_conversion.split(" to ")
                print(f"\n{value:.2f} {from_unit} = {result:.2f} {to_unit}")
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
