# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# Calculate velocity: D/t aka distance/time 
distance_in_miles = 10
time_in_min = 30.5 

velocity = distance_in_miles / time_in_min

# convert velocity from mi/m to km/hr to get speed 
speed = 1.6 * (velocity * 60) 
print(speed)