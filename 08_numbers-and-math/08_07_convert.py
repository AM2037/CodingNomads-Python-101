# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

a = 6
b = 126.40

# convert int —> float
print(float(a))

# convert float —> int
print(int(b))

# Divide float by int (now switched)
print(a/b) 

# Multiply float and int
print(a*b)

# Information lost: the numbers after the 
# decimal from the initial float variable b —> .40