# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
 
# Prompt user for string of words
words = input("Please enter random sentence here: ")
letter = input("Please type one letter from previous sentence here: ")

# Get index of first occurrence of letter in word
result = words.index(letter)

# Convert index (int) to str
print("Result: " + str(result))
