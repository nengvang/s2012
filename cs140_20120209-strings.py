"""Four score and seven years ago our fathers brought forth on this
continent a new nation, conceived in Liberty, and dedicated to
the proposition that all men are created equal."""

age = ''

while not age.isdigit():
    age = raw_input('Please enter your age: ')

age = int(age)
print 'You are', age, 'years old.'

