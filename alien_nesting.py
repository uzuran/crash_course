# Make an empty list for storing aliens.

aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change first 3 aliens, color, points, speed

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'


# Show first 5 aliens.

for alien in aliens[:6]:
    print(alien)
print('....')

# Show how many aliens are created.
print('Total number of aliens: ' + str(len(aliens)))
