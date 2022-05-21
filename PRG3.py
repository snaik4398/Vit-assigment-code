"""Length of diagonal in Rectangle

The perimeter of a rectangle is 46cm. If the length of the rectangle is 15cm, then what is the length of the diagonal
of the rectangle? (Hint: use Pythagorus theorem to solve). """

import math
perimeter = int(input("Enter the perimeter of the rectangle: "))
length = int(input("Enter the length of the rectangle: "))
breadth = (perimeter / 2) - length
diagonal = math.sqrt(length**2 + breadth**2)
print(f"Length of Diagonal= {diagonal}")

