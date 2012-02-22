# Things we need (should know)
#
# print
#   Display a blank line with an empty print statement
#       print
#   Display a single item on a separate line
#       print item
#   Display multiple items on a line with commas (,) separated by spaces
#       print item1, item2, item3
#       print item,
#
# raw_input([prompt])
#   Prompt users for text-based (str) information
#       Optional message
#       Blocking call
#       value = raw_input('Enter your name: ')
#       value = raw_input()
#
# Data Types
#   int, str, float, bool, list, dict
#   Each holds a different type of information and has related operators
#   Each also provides a creation/conversion function
import math

height = float(raw_input('Enter the height of the cylinder: '))
radius = float(raw_input('Enter the radius of the cylinder: '))
volume = 2 * math.pi * radius ** 2 * height
print 'The volume of a cylinder with height', height, 'and radius', radius,
print 'is', volume
