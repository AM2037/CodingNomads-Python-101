# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

# Prompt user for string of words
words = input("Please enter a random sentence: ")

# Prompt user for symbol
sym = input("Please enter a symbol: ")

# Identify value of first letter
first = words[0]

# Find all occurrences of the first letter
all_occ = [i for i, x in enumerate(words) if x == first]

# Replace all occurrences of first letter with provided symbol
chars = list(words)

for idx in all_occ:
    chars[idx] = sym

sym_words = ''.join(chars)
print(sym_words)

        







