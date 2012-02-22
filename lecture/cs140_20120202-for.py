# 2012-02-02

# range() function [built-in]
"""
>>> range
<built-in function range>
>>> help(range)
Help on built-in function range in module __builtin__:

range(...)
    range([start,] stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
"""
# Version 1
for lady in range(7):
    for cat in range(7):
        print lady, cat

# Version 2
for lady in range(7):
    print 'Lady', lady + 1,
    for cat in range(7):
        print 'Cat', cat + 1,
    print

