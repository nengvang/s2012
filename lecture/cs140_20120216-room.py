# Marcus M. Darden
# cs140_20120216-room.py
# Example for using variables versus constants

room_length = 21
room_width = 21

# Print the entire room on the screen
##for ii in range(room_length):            # Loop for room length (y-axis)
##    for jj in range(room_width):         # Loop for room width (x-axis)
##        print '0',
##    print

# This is the next thing: Basic printing of big room
x = 3
y = 1

br_len = 7
br_wid = 7

# Print the room and user's location (X)
for i in range(br_len / 2, -(br_len + 1) / 2, -1):      # Loop for y-axis
    for j in range(-(br_wid / 2), (br_wid + 1) / 2):    # Loop for x-axis
##        print j, i,     # Displays floor coordinates
        if i == y and j == x:                           # This is the user's location
            print 'X',
        else:                                           # Basic floor tile
            print '0',
    print

