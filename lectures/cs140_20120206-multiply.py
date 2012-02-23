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
    sign = -1
else:
    sign = 1

# Variable for final product
product = 0

while b != 0:
    # Determine if value is even or odd
##    if b / 2 * 2 == b:
##        pass
##    else:
##        print 'B is odd'

    if b / 2 * 2 != b:      # if b is odd
        product = product + a
    a *= 2                  # same as a = a * 2
    b /= 2

product *= sign
print 'The product is', product
