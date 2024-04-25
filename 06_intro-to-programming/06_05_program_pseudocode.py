# Think about a task that you want to accomplish using programming
# Maybe you want to automate something you do every day on your computer?
# Break down some of the steps you can think of and write them in
# this file as pseudocode.
# You can come back and update this file when you've learned more.
# You can also add real Python code after learning the necessary concepts.
# For now, just practice breaking larger tasks into smaller steps
# and writing out your thoughts in pseudocode.

# A shopping list calculator I built for one of the later sections of this course 
# since I prefer to work on the labs after completing several sections:

# Sephora shopping list accounting for discounted prices
# Create dictionary of hypothetical cost for items (in dollars)
prices = {
  "Refy Lip Sculpt Kit": 26.00,
  "Nars Soft Matte Concealer": 26.00,
  "Kaima Cosmetics Glitter": 15.00,
  "Lilly Lashes Inviting": 12.00,
  "Refy Brow Gel": 25.00
}

print(prices.keys())
print(prices.values())

# Loop through items - only apply 25% discount to merch under $20.00
discounted_prices = {k:v - v * .25 for (k,v) in prices.items() if v<=20.00}

print(discounted_prices) # 11.25, 9.00 new prices

# update first dictionary with new updated values
prices.update(discounted_prices)

# Display results
print(prices)