# Exercise 1
# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
'pyscript' == 'PyScript'

# Compare a boolean with an integer
True == 1

# Exercise 2
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print("test" <= y)

# Comparison of booleans
print(True > False)

# Exercise 3
# Create arrays
import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# Exercise 4
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2 * my_kitchen < 10 and 3 * your_kitchen)

# Exercise 5
# Create arrays
import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Exercise 6
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit":
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print('big place!')

# Exercise 7
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
else:
    print("looking around elsewhere.")

# if-else construct for area
if area > 15:
    print("big place!")
else:
    print('pretty small.')

# Exercise 7
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
else:
    print("looking around elsewhere.")

# if-else construct for area
if area > 15:
    print("big place!")
elif area > 10:
    print('medium size, nice!')
else:
    print('pretty small.')
