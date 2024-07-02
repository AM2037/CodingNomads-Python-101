# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# Prompt user for number within specified range
num = int(input("Please enter a number between 0 and 1,000,000,000: "))

# If user enters number:
while True:
    # and number is within range:
    for i in range(0,1000000001):
        # find and print number
        num_search = num.find(i) # fix AttributeError
        print(num_search)
        break
    else: 
        print("Please enter valid number: ")
        continue