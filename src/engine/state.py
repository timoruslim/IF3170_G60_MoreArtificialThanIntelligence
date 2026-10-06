import copy
import random
from .constraints import is_valid

class Placement:

   def __init__(self, truck_id=None, x=0, y=0, z=0, orientation=0):
      self.truck_id = truck_id
      self.x = x
      self.y = y
      self.z = z
      self.orientation = orientation

   def copy(self):
      return Placement(
         truck_id = self.truck_id,
         x = self.x,
         y = self.y,
         z = self.z,
         orientation = self.orientation
      )

   def __str__(self):
      if self.truck_id is None:
         return "Unassigned"
      return f"Truck {self.truck_id} at ({self.x}, {self.y}, {self.z})"

   __repr__ = __str__

class State:
   
   def __init__(self, packages, trucks, init="outside"):
      self.packages = packages
      self.trucks = trucks
      self.placements = {}
      self.initialize_placements(init)

   def initialize_placements(self, init):

      match init:

         case "outside":
            for package in self.packages:
               self.placements[package.id] = Placement()
         
         case "random":
            for package in self.packages:
               truck = random.choice(self.trucks + [None])
               if truck is None:
                  self.placements[package.id] = Placement()
               else:
                  orientation = random.randint(0, 5)
                  dx, dy, dz = package.get_dimensions(orientation)

                  max_x = truck.width - dx
                  max_y = truck.length - dy
                  max_z = truck.height - dz

                  x = random.randint(0, max_x) if max_x > 0 else 0
                  y = random.randint(0, max_y) if max_y > 0 else 0
                  z = random.randint(0, max_z) if max_z > 0 else 0
                  
                  self.placements[package.id] = Placement(truck_id=truck.id, x=x, y=y, z=z, orientation=orientation)

         case "random_feasible":
            for package in self.packages:
               while True:
                  truck = random.choice(self.trucks + [None])
                  if truck is None:
                     self.placements[package.id] = Placement()
                  else:
                     orientation = random.randint(0, 5)
                     dx, dy, dz = package.get_dimensions(orientation)
   
                     max_x = truck.width - dx
                     max_y = truck.length - dy
                     max_z = truck.height - dz

                     x = random.randint(0, max_x) if max_x > 0 else 0
                     y = random.randint(0, max_y) if max_y > 0 else 0
                     z = random.randint(0, max_z) if max_z > 0 else 0
                     
                     self.placements[package.id] = Placement(truck_id=truck.id, x=x, y=y, z=z, orientation=orientation)
                  if is_valid(self):
                     break

   def get_placement(self, package_id):
      return self.placements[package_id]

   def set_placement(self, package_id, placement):
      self.placements[package_id] = placement

   def get_packages_in_truck(self, truck_id):
      return [
         (package, self.placements[package.id]) for package in self.packages
         if (placement := self.placements.get(package.id)) is not None and placement.truck_id == truck_id
      ]

   def get_packages_not_outside(self):
      return [
         package for package in self.packages
         if self.placements[package.id].truck_id != None
      ]

   def get_packages_outside(self):
      return [
         package for package in self.packages
         if self.placements[package.id].truck_id == None
      ]

   def copy(self):
      new_state = State(self.packages, self.trucks)
      new_state.placements = {package_id: placement.copy() for package_id, placement in self.placements.items()}
      return new_state

   def __str__(self):
      result = "State:\n"
      for package in self.packages:
         placement = self.placements[package.id]
         result += f"  {str(package)} -> {str(placement)}\n"
      return result

   __repr__ = __str__
