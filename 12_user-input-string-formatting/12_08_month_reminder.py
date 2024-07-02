# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement. -- Tried this, changing approach to be more concise

# Assigning month numbers to their respective names via dictionary instead
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10:  'October',
    11:  'November',
    12: 'December'}

# If number user entered is in range, print corresponding month name
while True:
    # Prompt user for number between 1 and 12
    mon = int(input("Please enter a number between (or equal to) 1 and 12: "))

    if 1 <= mon <= 12:
        print(months[mon])
        break
    else:
        print("Please enter a valid number.")
    # Repeat loop
    continue