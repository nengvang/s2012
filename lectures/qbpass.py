# In football, there is a statistic for quarterbacks called the passer rating.
# To calculate the passer rating, you need five inputs: pass completions, pass
# attempts, total passing yards, touchdowns, and interceptions. There are five
# steps in the algorithm. Write a program that asks for the five inputs and
# then prints the passer rating:
#    a) C is the "completions per attempt" times 100 - 30 all divided by 20
#    b) Y is the "yards per attempt" - 3 all divided by 4
#    c) T is the "touchdowns per attempt" times 20
#    d) I is 2.375 minus ("interceptions per attempt" times 25)
#    e) The passer rating is the sum of C, Y, T, and I all divided by 6 and
#       then multiplied by 100

# Request four statistical inputs
completions = raw_input('Enter the number of completed passes: ')
attempts = raw_input('Enter the number of attempted passes: ')
total_yards = raw_input('Enter the number of total passing yards: ')
touchdowns = raw_input('Enter the number of touchdown passes: ')
interceptions = raw_input('Enter the number of interceptions: ')

# Calculate intermediate values
C = (((float(completions) / float(attempts)) * 100) - 30) / 20
##print 'C:', C
Y = ((float(total_yards) / float(attempts)) - 3) / 4
##print 'Y:', Y
T = (float(touchdowns) / float(attempts)) * 20
##print 'T:', T
I = 2.375 - ((float(interceptions) / float(attempts)) * 25)
##print 'I:', I

# Combine intermediates to get passer rating
rating = ((C + Y + T + I) / 6) * 100
print 'QB Passer Rating:', rating
