# bmi_calculator.py

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight (kg) / height (m)^2."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to calculate and display BMI."""
    print("Welcome to the BMI Calculator!")
    
    try:
        # Get user input
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        
        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers. Please try again.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Get BMI category
        category = categorize_bmi(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
