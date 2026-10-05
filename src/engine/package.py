class Package:

   def __init__(self, id, width, length, height, value, weight, is_fragile, eta):
      self.id = id
      self.width = width
      self.length = length
      self.height = height
      self.value = value
      self.weight = weight
      self.is_fragile = is_fragile
      self.eta = eta

   def get_dimensions(self, orientation=0):
      w, l, h = self.width, self.length, self.height
      orientations = [
         (w, l, h),
         (w, h, l),
         (l, w, h),
         (l, h, w),
         (h, w, l),
         (h, l, w)
      ]
      return orientations[orientation]

   def __str__(self):
      return f"Package {self.id} (dim={self.width}x{self.length}x{self.height}, weight={self.weight}, value={self.value}, fragile={self.is_fragile}, eta={self.eta})"

   __repr__ = __str__