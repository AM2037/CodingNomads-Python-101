import re

# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
name = input("Please enter your name: ")

# Check if multiple words in string i.e. first and last names
name_length = len(name)

# Find # of spaces aka seperator between words
spaces = len(re.findall(r'\s+', name))

if (spaces + 1) == 1:
    print("Only first name given")
else: 
    print("This is a first and last name.")