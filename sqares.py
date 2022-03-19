# Some example of square numbers

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)


squares2 = []
for value in range(1, 11):
    squares2.append(value ** 2)

squares3 = [value ** 2 for value in range(1, 11)]

print(squares3)
