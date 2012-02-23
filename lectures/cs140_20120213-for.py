for i in range(10):
    for j in range(10):
        print i, j,
    print

print
for i in range(10):
    for j in range(10):
        print '(', i, j, ')',
    print

# This has 'inverted' axes
print
for x in range(10):
    for y in range(10):
        print '(', x, y, ')',
    print

# This has 'proper' axes
print
for y in range(10):
    for x in range(10):
        print '(', x, y, ')',
    print

# Looking at time
print
for hour in range(1, 13):
    for minute in range(1, 61):                 # Minutes are broken
        print str(hour) + ':' + str(minute)

# Looking at time
print
for hour in range(1, 13):
    for minute in range(60):                    # Minutes are fixed
        print str(hour) + ':' + str(minute),
    print

# More on time
print
for hour in range(1, 13):
    print 'It\'s', hour, 'O\'clock!'
    for minute in range(60):                    # Minutes are fixed
        print str(hour) + ':' + str(minute),
    print

# Triangles
print
for i in range(10):
    for j in range(i + 1):
        print '*',
    print

print
for i in range(10):
    for j in range(0, (10 - i) * 5, 5):
        print '*',
    print



