# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to string to easily find the length (number of digits)
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return sum_of_powers == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display if the number is Armstrong or not
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
