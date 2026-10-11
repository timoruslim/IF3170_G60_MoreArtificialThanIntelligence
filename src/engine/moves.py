import random
from .state import Placement

def swap_packages(state, package_id_a, package_id_b):
   new_state = state.copy()

   placement_a = new_state.get_placement(package_id_a)
   placement_b = new_state.get_placement(package_id_b)

   new_state.set_placement(package_id_a, placement_b)
   new_state.set_placement(package_id_b, placement_a)

   return new_state

def move_package(state, package_id, new_placement):
   new_state = state.copy()
   new_state.set_placement(package_id, new_placement)

   return new_state


def rotate_package(state, package_id, new_orientation):
   new_state = state.copy()
   placement = new_state.get_placement(package_id)
   placement.orientation = new_orientation
   new_state.set_placement(package_id, placement)

   return new_state

def get_random_neighbor(state):

   move = random.randint(0, 2)

   match move:

      # Swap
      case 0:
         package_a, package_b = random.sample(state.packages, 2)
         return swap_packages(state, package_a.id, package_b.id)

      # Move 
      case 1:
         package = random.choice(state.packages)
         truck = random.choice(state.trucks + [None])

         if truck is None:
            new_placement = Placement()
         else:
            orientation = random.randint(0, 5)
            dx, dy, dz = package.get_dimensions(orientation)

            max_x = truck.width - dx
            max_y = truck.length - dy
            max_z = truck.height - dz

            x = random.randint(0, max_x) if max_x > 0 else 0
            y = random.randint(0, max_y) if max_y > 0 else 0
            z = random.randint(0, max_z) if max_z > 0 else 0
            
            new_placement = Placement(truck_id=truck.id, x=x, y=y, z=z, orientation=orientation)

         return move_package(state, package.id, new_placement)

      # Rotate
      case 2:
         package = random.choice(state.packages)
         placement = state.get_placement(package.id)
         if placement.truck_id is None: 
            return get_random_neighbor(state) 
         
         new_orientation = random.randint(0, 5)
         return rotate_package(state, package.id, new_orientation)

def get_all_neighbors(state):
   neighbors = []

   # Swap
   for i in range(len(state.packages)):
      for j in range(i + 1, len(state.packages)):
         package_a = state.packages[i]
         package_b = state.packages[j]
         neighbors.append(swap_packages(state, package_a.id, package_b.id))

   # Move
   for package in state.packages:
      for truck in state.trucks + [None]:
         if truck is None:
            new_placement = Placement()
            neighbors.append(move_package(state, package.id, new_placement))
         else:
            for orientation in range(6):
               dx, dy, dz = package.get_dimensions(orientation)

               max_x = truck.width - dx
               max_y = truck.length - dy
               max_z = truck.height - dz

               for x in range(max_x + 1):
                  for y in range(max_y + 1):
                     for z in range(max_z + 1):
                        new_placement = Placement(truck_id=truck.id, x=x, y=y, z=z, orientation=orientation)
                        neighbors.append(move_package(state, package.id, new_placement))

   # Rotate
   for package in state.packages:
      for orientation in range(6):
         neighbors.append(rotate_package(state, package.id, orientation))

   return neighbors