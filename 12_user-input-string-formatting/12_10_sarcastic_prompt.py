# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

'''
The following prompts user for their honest opinion about something and
then converts all the letters to lowercase for proper alternating caps.
'''

op = input("What do you honestly think about pinapple on pizza?").lower()

# Using list comprehension to only capitalize every other letter in response
sarcasm = "".join([char.upper() if i % 2 else char for i,char in enumerate(op)])

# Print sarcastic style response
print(sarcasm)