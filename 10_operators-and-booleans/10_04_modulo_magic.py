# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.
num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997

nums = [num_1, num_2, num_3, num_4]

for num in nums:
    if num % 7 == 0:
        print(num)
