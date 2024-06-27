# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
name = input("Please enter your name: ")

# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
if len(name).split() > 1: # AttributeError: 'int' object has no attribute 'split'
    last_name = name[1]
    print(f"Welcome {last_name}.")
else:
     print(f"Welcome {name}.")