# Tuple
#   Collections
#   Iterable
#   Index-able
#   Sliceable
#   Immutable (different from lists)
#   Created with parenthesis () and commas ,
#   Holds any homogenous data
#   Methods: count & index

# Examples
('Olivet', 'College', 'Comets')
(3, 4, 5)
('Olivet College', 1844)
('College', 1844, True, [2, 3, 4], (3, 4))


# Subprograms (functions, Chapter 5)
#   Created with the def keyword
#   Use indenting to show structure
#   The colon (:) begins the body/suite
#   Optional list of arguments
#   Arguments may default values (advanced)
#   Variable numbers of args may be used (very advanced)
#   Used for two reasons: return values & side effects (can be both)
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

large = find_largest(4, 10)
print 'The largest is', large

def find_largest3a(a, b, c):
##    if a > b:
##        return a
##    else:
##        return b
##    if a > c:
##        return a
##    else:
##        return c
##    if b > c:
##        return b
##    else:
##        return c
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif a == b and a > c:
        return a
##    elif b == c and b > a:
##        return b
##    elif a == c and a > b:
##        return a
    else:
        return c

def find_largest3b(a, b, c):
    if a >= b:                  # Only between a & c
        if a > c:
            return a
        else:
            return c
    else:                       # Only between b & c
        if b > c:
            return b
        else:
            return c


def find_largest3c(a, b, c):
    if find_largest(a, b) == a:
        return find_largest(a, c)
    else:
        return find_largest(b, c)


def say_hello():
    print 'Hello, World!'
