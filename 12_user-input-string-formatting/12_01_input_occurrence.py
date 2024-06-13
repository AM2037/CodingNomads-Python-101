# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
 
# Prompt user for string of words
words = input("Please enter random sentence here: ")
letter = input("Please type one letter from previous sentence here: ")

result = words.index(letter)

print(f"Result: " + {result}) 
# TODO: Fix TypeError: can only concatenate str (not "set") to string