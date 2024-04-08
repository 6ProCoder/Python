# This program calculates the sum, product, and average of a list of numbers.
import time
# Get the number of numbers from the user.
play = input("Enter the number of numbers: ")

# Create a list to store the numbers.
numbers = []

# Get the numbers from the user.
for i in range(int(play)):
    number = input("Enter a number: ")
    numbers.append(float(number))

# Calculate the sum, product, and average of the numbers.
sum = 0
product = 1
for number in numbers:
    sum += number
    product *= number
average = sum / len(numbers)

# Print the results.
print("The sum is:", sum)
print("The product is:", product)
print("The average is:", average)
time.sleep(20)
