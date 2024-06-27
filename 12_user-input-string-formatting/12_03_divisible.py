# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

# Write a program that takes a number between 1 and 1,000,000,000
num = int(input("Please enter a number between 1 and 1,000,000,000: "))

# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
if num % 3:
    print(num)
else:
    print("This number is not divisible by 3!") 
# TODO: DEBUG -- tried 26 and it's returning 26 even though not divisible by 3