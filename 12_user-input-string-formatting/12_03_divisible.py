# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

# Prompt user for number between 1 and 1,000,000,000
num = int(input("Please enter a number between 1 and 1,000,000,000: "))

# Check if divisible by 3
if (num % 3) == 0:
    print(num)
else:
    print("This number is not divisible by 3!")