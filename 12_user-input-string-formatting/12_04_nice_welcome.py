import re

# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
name = input("Please enter your name: ")

# Check if multiple words in string i.e. first and last names
name_length = len(name)

# Find # of spaces aka seperator between words
spaces = len(re.findall(r'\s+', name))

# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
if (spaces + 1) == 1:
    print(f"Welcome, {name}!")
else: 
    first_name = name.split(" ")[0]
    print(f"Welcome, {first_name}!")