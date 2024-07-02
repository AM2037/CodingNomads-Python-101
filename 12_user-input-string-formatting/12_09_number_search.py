# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# Prompt user for number within specified range
num = int(input("Please enter a number between 0 and 1,000,000,000: "))

# Check if number in range
while True:
    if num not in range(0,1000000001):
        print(int(input("Please enter valid number: ")))
    # If number in range
    else: 
        # Print number
        print(num)
        break

# TODO: Works but repeating second prompt after entering valid number
# in cases where user enters invalid number first -- handle