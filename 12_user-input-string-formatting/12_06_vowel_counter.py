# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Prompt user for a sentence
input_string = str(input("Please enter any sentence here."))

# Declare vowels
vowels = "aeiou"

def count_vowels(input_string, vowels):

# Trying comprehension instead
    vowel_counter = [char for char in input_string if char in vowels]
    total_count = len(vowel_counter)
    print(f"The total number of vowels is: {total_count}")

count_vowels(input_string, vowels)