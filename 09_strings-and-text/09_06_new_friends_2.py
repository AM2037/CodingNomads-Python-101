# Write code that produces a TypeError when you run this script.
count = 16

# Reusing shopping list code from section 6 labs

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
# discounted_prices = {k:v - v * .25 for (k,v) in prices.items() if v<=20.00} # working dictionary comprehension code
discounted_prices = {prices.values - prices.values * .25 for (k,v) in prices.items 
                     if prices.values <= 20.00} # produces TypeError: 'builtin_function_or_method' object is not iterable

print(discounted_prices) # 11.25, 9.00 new prices

# update first dictionary with new updated values
prices.update(discounted_prices)

# Display results
print(prices)