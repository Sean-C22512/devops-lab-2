numbers = input("Enter numbers separated by space: ").split()
numbers = [float(num) for num in numbers]
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")