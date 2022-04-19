# This test file is to be used to test shapes.py development. 
# It already contains a few examples of things to check.
# Start by reading README.md
import shapes

if (issubclass(shapes.Square, shapes.Rectangle)):
    print("Square is a child of Rectangle")
else:
    print("Square is NOT a child of Rectangle")

# Setup for output as seen in README.md
rect = shapes.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shapes.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
