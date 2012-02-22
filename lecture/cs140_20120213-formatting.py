# More on strings

# String operators
"""The comparison operators <, >, <=, >=, ==, != can be used on strings.

They work on things in a dictionary sense.

>>> 'a' > 'b'
False
>>> 'four' > 'fourteen'
False
>>> 'for' > 'fourteen'
False
>>> 'A' > 'a'            # See ASCII table
False


The in operator looks for membership in a sequence.
"""

# Formatting strings
"""Using string formatting:

'<format string>' % (data1, data2, ...)

Format string placeholders:
    %s      For strings         (str)
    %d      For integers        (integers)
    %f      For real numbers    (float)

Full formatting syntax
    %[name][flags][width][.precision]code

"""


# A while loop, with the optional trailing else clause
val = ''
while val != 'q':
    val = raw_input('input: ')
    print 'You entered', val
    if val.isdigit():
        break
else:
    print 'Goodbye'
