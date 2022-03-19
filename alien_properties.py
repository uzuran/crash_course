alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print('Original x_position: ' + str(alien_0['x_position']))

# del y_position kay
del alien_0['y_position']

# Move the alien to the right.
# Determine how far to move the alien base on its current speed.


if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3     # Must be a fast alien


# The new position is old position plus the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New position: ' + str(alien_0['x_position']))
print(alien_0)

