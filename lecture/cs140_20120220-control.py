# More on loop control structures
#
# Three keywords to go with for and while
# 1. else
#   Works similar to how else does, with if, executed at the end.
#   Works different to how else does, with if, not necessarily mutually exclusive.
i = 0
while i < 10:
    i = int(raw_input('Enter a number: '))
else:
    print 'That number was too large.'
print

for a in range(10):
    print a
else:
    print 'We\'re done!'
print

# 2. break
#   Moves execution out of the nearest loop, immediately!
#   Skips any existing else clause.
i = 0
while i < 10:
    i = int(raw_input('Enter a number: '))
    if i < 0:
        print 'That was pretty negative...'
        break
    print 'Thanks alot!'
else:
    print 'That number was too large.'
print

direction = ''
while True:
    print 'some stuff'
    direction = raw_input('Enter a direction: ')
    if direction == 'n':
        print 'you head north'
    elif direction == 's':
        print 'you head south'
    elif direction == 'q':
        print 'let\'s get outta here...'
        break
print

# 3. continue
#   Jumps to the top of the current loop, and executes from there
for a in range(10):
    if a == 6:
        continue
    print '* ' * a
