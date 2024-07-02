# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# Prompt user for number within specified range
num = int(input("Please enter a number between 0 and 1,000,000,000: "))
start, stop = 0, 1000000001
# Check if number in range
while True:
    if num not in range(start, stop):
        print(int(input("Please enter valid number: ")))
        break
    if num in range(start, stop):
        # If number in range, print number
        print(num)
        break