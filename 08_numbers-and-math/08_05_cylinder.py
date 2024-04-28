# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

from math import pi
# Calculate area of base * height of cylinder 
# Cylinder volume formula: V = π r² h 
r = 3.14
h = 5
V = pi * r**2 * h

print(V)

# Calculate 2(Base) + Rectangle (aka "unfolded" cylinder)
# Cylinder surface formula: SA = 2πrh + 2πr²
SA =  (2 * pi * r * h) + (2 * pi * r**2)
print(SA)