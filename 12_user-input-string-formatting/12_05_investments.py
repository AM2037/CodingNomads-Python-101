# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

# Prompt user for the following to be used in the formula shown above
present_value = int(input("Please enter amount you plan to  invest: "))
int_rate_prompt = float(input("What is the interest rate? "))
# Convert interest rate response into percentage
int_rate = int_rate_prompt / 100
num_years = int(input("How long do you plan to invest, in years?:  "))

# Formula:
# future value = present value x (1 + (interest rate * n)) where n = num years

# Calculate appreciation rate first (second half of equation)
app_rate = 1 + (int_rate * num_years)
future_value = present_value * app_rate

# Print result
print(f"The estimated future value of this investment is: {future_value}")