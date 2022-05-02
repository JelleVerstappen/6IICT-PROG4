## Assignment
Complete the `Rectangle` and `Square` classes in `finances.py`.
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a child of Rectangle and inherit methods and property.

### Rectangle class
When a Rectangle object is created, it should be initialized with `width` and `height` property. The class should also contain the following methods:
* `set_width()`
* `set_height()`
* `get_area()`: Returns area (`width * height`)
* `get_perimeter()`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal()`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture()`: Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should instead return the string: "Too big for picture.".
* `get_amount_inside()`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4. Should return an error message if the shape does not fit.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)` 
TIP: use `__repr__()` as seen in "Finance Tracker".

### Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__()` method should store the side length in both the `width` and `height` property from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side()` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width()` and `set_height()` methods on the Square class should set both the width and height.

### Usage example
```py
rect = shape.Rectangle(10, 5)
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
```

That code should return:
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

#### Implementation

You can test shapes.py using the examples given in `test.py`. Afterwards in `main.py` add the following shapes:

* `rect` : 22 x 5
* `square`: 8 x 8

Print following things for both shapes:
* `rect` and `square` themselves
* `perimeter`
* `area`
* `diagonal`
* `How many times square fits in rect`
* `picture`

This should return:

```
Rectangle(width=22, height=5)
54
110
22.561028345356956
Shape did not fit
**********************
**********************
**********************
**********************
**********************


Square(side=8)
32
64
11.313708498984761
********
********
********
********
********
********
********
********
```

Afterwards. Change the dimensions of `rect` and `square` to 51x8 and 4x4,
using the methods defined in the classes. Once again print what was mentioned above. The result should be as follows.

```
4
Rectangle(width=8, height=51)
118
408
51.62363799656123
24
Too big for picture.

Square(side=4)
16
16
5.656854249492381
****
****
****
****
```

### Extra
Create a new class Diamond (Nl: Ruit). This should be a child class of Rectangle. When a Diamond object is created, two parameters are passed in. One for the distance between the two side points, one for the distance between the top and bottom points (see image below). The `__init__()` method should store these length respectively as the `width` and `height` property from the Rectangle class.

<p align="center">
  <img src="diamond.png" width="200" height="300"/>
</p>

The Diamond class should be able to access the Rectangle class methods but should also contain a `get_line()` method which gives the length between a side and the top/bottom point. Additionally `get_diagonal()` should be deprecated since this was passed in, when a Diamond object was created. `get_picture()`, `get_perimeter()` and `get_area()` need to be reworked in order to print a diamond. 

`get_picture()` will not be able to properly print all diamonds. It should however be one wide at the top and bottom and the size of the width at the middle. It should also be mirrored around the x- and y-axis. Assume that all values of width and height are uneven. This will make it easier to create the picture.

If an instance of a Diamond is represented as a string, it should look like: `Diamond(width=8, height=4)`


#### Implementation
Test the Diamond class by creating the following shapes:

* `rect` : 22 x 10
* `diamond`: 4 x 8 

Print following things of diamond:
* `diamond` itself
* `perimeter`
* `area`
* `diagonal`
* `line`
* `How many times diamond fits in rect`
* `picture`

This should return:

```
Diamond(width=5, height=9)
37.36308338453881
22.5
Method deprecated through definition of width and height
5.1478150704935
4
  *
  *
 ***
 ***
*****
 ***
 ***
  *
  *
```