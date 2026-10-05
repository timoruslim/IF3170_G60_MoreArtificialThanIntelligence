import copy

class Placement:

   def __init__(self, truck_id=None, x=0, y=0, z=0, orientation=0):
      self.truck_id = truck_id
      self.x = x
      self.y = y
      self.z = z
      self.orientation = orientation

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
