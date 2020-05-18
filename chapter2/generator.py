import array

# We're going to  use a tuple  and then an array 


symbols = '!@#$%^'
# This will initialize a tuple with all of the values in the sybpl as ordinals
print(tuple(ord(symbol) for symbol in symbols))

#  The array contructor takes 2 arguments the first defines a storage type
tuple_ordinal = array.array('I', (ord(symbol) for symbol in symbols))

print(tuple_ordinal)

# Let's use a generator to print tshirts and sizes

colors = ['Red', 'Blue']

sizes = ['S', 'M', 'L']

for shirt in (f'{color}, {size}' for color in colors for size in sizes):
    print(shirt)