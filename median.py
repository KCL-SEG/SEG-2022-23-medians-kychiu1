"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
i = 0
j = len(numbers) - 1
while i < j:
    i += 1
    j -= 1
median = (numbers[i] + numbers[j]) / 2
print(median)
