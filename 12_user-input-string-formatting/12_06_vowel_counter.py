# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Prompt user for a sentence
input_string = str(input("Please enter any sentence here: "))

# Declare vowels
vowels = "aeiou"

freq = {}.fromkeys(vowels, 0)

def vowel_freq(input_string, vowels):
    # Get frequency of only vowels
    for char in input_string:
        if char in vowels:
            freq[char] += 1

    return freq

frequency = vowel_freq(input_string, freq)
print(f"The total number of times each vowel appears is: {frequency}")
