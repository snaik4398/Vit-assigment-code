"""Consider the thirsty crow story where a thirsty crow identifies a jug with little water. It puts pebbles into the
water to raise the level of water and drinks it. Assume that the initial reading of the jug is 'm1' ml and the crow
can drink water if the level of water has come to 'm2' ml.  There are two categories of pebbles small and big in the
field. Small pebble can raise the level of water by 'x' ml and big pebble can raise the level of water by 'y' ml.
There are 'n' small pebbles. Crow prefers to place small pebbles in jug and then only takes big pebbles. Write an
algorithm and the Python code to determine the number of pebbles required to raise the water to ‘m2’ level. For
example, if value of 'm1', 'm2','x','y' and  'n' are 54, 300, 10, 20, 10 respectively then the number of pebbles
required is 13. """

initial_level = 54
required_level = 300
height_increased_by_small_pebbles = 10
height_increased_by_big_pebbles = 20
number_of_small_pebbles = 10

raise_level = required_level - initial_level
print(f"Raise Level: {raise_level}")
raised_by_small_pebbles = raise_level/number_of_small_pebbles * height_increased_by_small_pebbles
print(f"Raised by small pebbles: {raised_by_small_pebbles}")
number_of_big_pebbles = (raise_level - raised_by_small_pebbles)/height_increased_by_big_pebbles

print(number_of_big_pebbles)
