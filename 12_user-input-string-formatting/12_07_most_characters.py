# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


# Prompt user for responses
message = str(input("Please enter a word or phrase: "))

# Set length of messages as it's own variable
length = len(message)

# Initialize variable to find longest string
longest = 0

# Declare empty list for storing messages aka user responses
messages = []

# Define a loop to run prompt 3 times
for index in range(3):
    # add response to list
    messages.append(message)

def find_longest(message):
    if len(message).max():
        print(f"{length} + "," + {message}")

print(messages) # TODO: Fix for loop -- currently just adding response to list 3 times