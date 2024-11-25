# BMI Calculator in Python

A simple Python program that calculates the Body Mass Index (BMI) based on user-provided weight and height. This project demonstrates basic Python programming concepts such as user input handling, mathematical calculations, conditional statements, and error handling.

## Introduction

The **BMI Calculator** is a beginner-friendly Python program that calculates BMI using the formula:

\[
\text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}
\]

It categorizes BMI into health ranges such as **Underweight**, **Normal weight**, **Overweight**, or **Obesity**, providing users with a clear interpretation of their BMI.

## Features

- Calculates BMI based on user input for weight (in kilograms) and height (in meters).
- Categorizes BMI into health ranges:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 ≤ BMI < 24.9
  - Overweight: 25 ≤ BMI < 29.9
  - Obesity: BMI ≥ 30
- Handles invalid inputs gracefully using error handling.

## Prerequisites

- Python 3.6 or higher installed on your system.
- A code editor such as **Visual Studio Code** or any Python IDE.

## Usage

1. **Run the Program**:
   - Open the terminal in Visual Studio Code by navigating to `View > Terminal`.
   - Ensure Python is installed by typing:
     ```bash
     python --version
     ```
   - Run the script:
     ```bash
     python bmi_calculator.py
     ```

2. **Input Data**:
   - Enter your weight in kilograms and height in meters when prompted.

3. **View Results**:
   - The program will display your calculated BMI and health classification.

## Code Walkthrough

### Functions

1. **`calculate_bmi(weight, height)`**:
   - Calculates BMI using the formula: 
     \[
     \text{BMI} = \frac{\text{Weight}}{\text{Height}^2}
     \]

2. **`categorize_bmi(bmi)`**:
   - Determines the health category based on the BMI value:
     - Underweight: BMI < 18.5
     - Normal weight: 18.5 ≤ BMI < 24.9
     - Overweight: 25 ≤ BMI < 29.9
     - Obesity: BMI ≥ 30

3. **`main()`**:
   - Manages the program flow:
     - Accepts user input.
     - Validates the input.
     - Calls the `calculate_bmi` and `categorize_bmi` functions.
     - Displays the results.

### Error Handling
- Invalid input (e.g., non-numeric or negative values) is handled using a `try-except` block to ensure the program doesn't crash.

