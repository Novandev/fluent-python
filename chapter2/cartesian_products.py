colors = ['Black', 'White', 'Blue']

numbers = [1, 2, 3]
 # This will match all colors to numbers
cartesian = [(color, number) for color in colors for number in numbers]

print(cartesian)