class Truck:

   def __init__(self, id, width, length, height, max_capacity):
      self.id = id
      self.width = width
      self.length = length
      self.height = height
      self.max_capacity = max_capacity

   def __str__(self):
      return f"Truck {self.id} (dim={self.width}x{self.length}x{self.height}, max_capacity={self.max_capacity})"

   __repr__ = __str__