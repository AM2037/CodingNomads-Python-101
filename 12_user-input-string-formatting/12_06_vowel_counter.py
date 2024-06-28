# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Prompt user for a sentence
input_string = str(input("Please enter any sentence here."))

# Initialize vowel counter
vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels(char, vowels): #could change to match call below if doesn't work

    for char in input_string:
        if char in vowels: # TypeError: argument of type 'int' is not iterable
           vowel_count += 1

total_vowel_count = count_vowels(input_string, vowel_count) # same TypeError here too

print(f"The total number of vowels is: {total_vowel_count}")
