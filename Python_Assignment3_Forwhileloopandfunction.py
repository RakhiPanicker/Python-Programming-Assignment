import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)

# Set maximum number of guesses allowed
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue
    elif guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break

    attempts -= 1
else:
    print("Better luck next time!")


# For Loop - Multiplication table Generator
# Prompt user for input
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and display the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")    

# Function: BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Prompt the user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Use the function to calculate and display the BMI
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")    