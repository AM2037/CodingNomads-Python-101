# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

# Prompt user for number between 1 and 12
mon = int(input("Please enter a number between (or equal to) 1 and 12: "))
# Assigning month name to number using enumerate 
mon_names = ['January', 'February', 'March', 'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']

mon = [mon_names[x] for x in mon] # TODO: Fix TypeError: 'int' object is not iterable
assign_names = {x: ind for ind, x in enumerate(set(mon_names))}

# Using nested if statement
for i in range(1,13):
    if 1 <= mon <= 12:
        print(mon_names[i])