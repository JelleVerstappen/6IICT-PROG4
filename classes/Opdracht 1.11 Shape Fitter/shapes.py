from importlib.util import set_loader


class Rectangle():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height


 

  def set_width(self, amount):
    self.width = amount
    return self.width

  def set_height(self, amount):
    self.height = amount
    return self.height
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return self.width * 2 + self.height * 2

  def get_diagonal(self):
    return (self.width ** 2 + self.height **2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big picture"

    w = ""
    for height in range(self.height):
      for width in range(self.width):
        w += "*"
      w +='\n'
    print(w)

  def get_amount_inside(self, shape):
    if shape.width > self.width and shape.height > self.width:
      return "Shape doesn't fit in this rectangle"
    
    fits_width = self.width // shape.width
    fits_height = self.height // shape.height

    return f"This shape fits {fits_width * fits_height} times in this rectangle"


class Square(Rectangle):
    def __init__(self, x, y, width, height):
       super().__init__(x, y, width, height)
      
    def set_side(self, amount):
      self.height = amount
      self. width = self.height
    
class Diamond(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

rect = Rectangle(1,1, 6, 4)
shape = Square(1, 1, 2, 2)
print(rect.get_amount_inside(shape))
print(rect.get_picture())
print(shape.get_diagonal())