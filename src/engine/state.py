import copy

class Placement:

   def __init__(self, truck_id=None, x=0, y=0, z=0, orientation=0):
      self.truck_id = truck_id
      self.x = x
      self.y = y
      self.z = z
      self.orientation = orientation

   def __str__(self):
      if self.truck_id is None:
         return "Unassigned"
      return f"Truck {self.truck_id} at ({self.x}, {self.y}, {self.z})"

   __repr__ = __str__

class State:
   
   def __init__(self, packages, trucks):
      self.packages = packages
      self.trucks = trucks
      self.placements = {}

      for package in packages:
         self.placements[package.id] = Placement()

   def get_placement(self, package_id):
      return self.placements[package_id]

   def set_placement(self, package_id, placement):
      self.placements[package_id] = placement

   def get_packages_in_truck(self, truck_id):
      return [
         (package, self.placements[package.id]) for package in self.packages
         if self.placements[package.id].truck_id == truck_id
      ]

   def get_packages_outside(self):
      return [
         package for package in self.packages
         if self.placements[package.id].truck_id == None
      ]

   def copy(self):
      new_state = State(self.packages, self.trucks)
      new_state.placements = copy.deepcopy(self.placements)
      return new_state

   def __str__(self):
      result = "State:\n"
      for package in self.packages:
         placement = self.placements[package.id]
         result += f"  {str(package)} -> {str(placement)}\n"
      return result

   __repr__ = __str__
