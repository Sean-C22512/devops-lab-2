# Initialize an empty list to store the numbers
numbers = []

# Get the number of inputs from the user
n = int(input("How many numbers will you enter? "))

# Loop to get user input
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Display the results
print(f"The largest number you entered is: {largest}")
print(f"The smallest number you entered is: {smallest}")

