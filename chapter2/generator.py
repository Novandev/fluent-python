import array

# We're going to  use a tuple  and then an array 


symbols = '!@#$%^'
# This will initialize a tuple with all of the values in the sybpl as ordinals
print(tuple(ord(symbol) for symbol in symbols))

tuple_ordinal = array.array('I', (ord(symbol) for symbol in symbols))

print(tuple_ordinal)