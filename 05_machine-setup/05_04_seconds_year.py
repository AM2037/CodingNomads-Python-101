# Use the interpreter to calculate how many seconds are in a year.
# Then write the code in this script file below this line.
""" 
The process of conversion:
Multiply by number of days in year by number of hours in day
Multiply the result by number of minutes in day -- used _ to access result in interpreter
Multiply the result by number of seconds in minute -- used _ to access result again in interpreter 
"""

# Set variables
days_in_year = 365
hours_in_day = 24
min_in_hour = 60
sec_in_min = 60

sec_in_year = days_in_year * hours_in_day * min_in_hour * sec_in_min
print(sec_in_year)