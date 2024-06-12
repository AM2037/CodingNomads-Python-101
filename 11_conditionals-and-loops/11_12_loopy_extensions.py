# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

# Using for loop

filename = "operators.pdf"

ext = [".", "p", "d", "f"]
search=[]

for i in ext:
    if(filename.find(i)>0):
        search.append(True)
    else:
        search.append(False)
print(search)

# Alternative approach using map instead of for loop for concise searching
def check_ext(filename, extension):
    return list(map(lambda x: x in set(filename), extension))

# Testing false case
filename = "operators.py"
extension = ['.', 'p', 'd', 'f']

print(check_ext(filename, extension))
