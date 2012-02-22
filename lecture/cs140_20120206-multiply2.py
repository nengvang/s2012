# cs140_20120206-multiply2.py
# Author: Marcus M. Darden
# Date: 2012-02-06
#
# Description:
#   Multiply two numbers together, using an ancient peasant method

# What do we need?

# While loop to continue until b == 0
# Variables for A and B
# Distinguish between even and odd
# Variable(s) for final product

## If A and B are 2 integers to be multiplied, we repeatedly multiply A by 2
## and divide B by 2, until B cannot be divided any further. During each step,
## whenever B is odd, we add the the corresponding A to the product.

# Variables for A and B
a = int(raw_input('Enter an integer to be multiplied: '))
b = int(raw_input('Enter an integer to be multiplied: '))

# In case B is negative, deal with the sign
if b < 0:
    b *= -1
    a *= -1

# Variable for final product
product = 0

while b:
    # if B is odd, add A
    if b % 2:               # if B is odd
        product += a
    a *= 2                  # same as a = a * 2
    b /= 2

print 'The product is', product
