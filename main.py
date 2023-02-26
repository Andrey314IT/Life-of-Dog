class Dog:
  height = 40
  age = 1
  color = "Black"
  weight = 3

  def __init__(self, type):
    self.type = type
  def get_older_1(self):
    self.age += 1
    self.weight += 2
    self.height += 10
