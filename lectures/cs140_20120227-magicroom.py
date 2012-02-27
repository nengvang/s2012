# Random numbers and pseudo-random sequences
#
# import random
#
# random.random() -> random float in range [0.0, 1.0)
# random.shuffle(x) -> x is scrambled in place
# random.randint(a, b) -> random integer in range [a, b]

room_size = 15
max_potions = 5

### Keep track of the potion
##potion_x = random.randint(1, 15)
##potion_y = random.randint(1, 15)

# Dead space
dead_space = [5, 10]

# Generate a random number of potions from 1 to 5
num_potions = random.randint(1, max_potions)
potions = []
for potion in range(num_potions):                   # Each randomly generated potion
    x = random.randint(1, room_size * 2)
    y = random.randint(1, room_size)
    potions += [[x, y]]

# Draw the room
for outer in range(room_size + 2):                  # The y-axis
    print '#',
    for inner in range(room_size * 2):              # The x-axis
        if outer == 0 or outer == room_size + 1:    # Draw the border of #
            print '#',
        elif [inner, outer] in potions:             # We've found a potion!
            print 'P',
        elif [inner, outer] == dead_space:          # Nothing here
            print ' ',
        else:                                       # Empty floor space
            print '-',
    print '#'
