def get_bounding_box(package, placement):
   dx, dy, dz = package.get_dimensions(placement.orientation)
   return (placement.x, placement.y, placement.z, placement.x + dx, placement.y + dy, placement.z + dz)

def check_capacity(packages_in_truck, truck):
   return sum(package.weight for (package, _) in packages_in_truck) <= truck.max_capacity

def check_boundary(packages_in_truck, truck):
   for (package, placement) in packages_in_truck:

      x1, y1, z1, x2, y2, z2 = get_bounding_box(package, placement)

      if x1 < 0 or y1 < 0 or z1 < 0:
         return False
      
      if x2 > truck.width or y2 > truck.length or z2 > truck.height:
         return False
      
   return True

def check_overlap(packages_in_truck):
   for i, (package_a, placement_a) in enumerate(packages_in_truck):

      x1_a, y1_a, z1_a, x2_a, y2_a, z2_a = get_bounding_box(package_a, placement_a)

      for j, (package_b, placement_b) in enumerate(packages_in_truck):
         if i >= j:
            continue

         x1_b, y1_b, z1_b, x2_b, y2_b, z2_b = get_bounding_box(package_b, placement_b)

         overlap_x = x1_a < x2_b and x1_b < x2_a
         overlap_y = y1_a < y2_b and y1_b < y2_a
         overlap_z = z1_a < z2_b and z1_b < z2_a

         if overlap_x and overlap_y and overlap_z:
            return False
         
   return True

def check_support(packages_in_truck):
   for (package_a, placement_a) in packages_in_truck:
      if placement_a.z > 0:

         x1_a, y1_a, z1_a, x2_a, y2_a, _ = get_bounding_box(package_a, placement_a)
         supported = False

         for (package_b, placement_b) in packages_in_truck:
            if package_a.id == package_b.id:
               continue
            
            x1_b, y1_b, _, x2_b, y2_b, z2_b = get_bounding_box(package_b, placement_b)

            overlap_x = x1_a < x2_b and x1_b < x2_a
            overlap_y = y1_a < y2_b and y1_b < y2_a
            touch_z = z1_a == z2_b

            if touch_z and overlap_x and overlap_y:
               supported = True
               break

         if not supported:
            return False 
   return True

def check_fragile(packages_in_truck):
   for (package_a, placement_a) in packages_in_truck:
      if package_a.is_fragile:

         x1_a, y1_a, _, x2_a, y2_a, z2_a = get_bounding_box(package_a, placement_a)

         for (package_b, placement_b) in packages_in_truck:
            if package_a.id == package_b.id:
               continue
            
            x1_b, y1_b, z1_b, x2_b, y2_b, _ = get_bounding_box(package_b, placement_b)

            overlap_x = x1_a < x2_b and x1_b < x2_a
            overlap_y = y1_a < y2_b and y1_b < y2_a
            touch_z = z1_b == z2_a

            if touch_z and overlap_x and overlap_y:
               return False
   return True

def is_valid(state):
   for truck in state.trucks:
      packages_in_truck = state.get_packages_in_truck(truck.id)
      if not check_capacity(packages_in_truck, truck): return False
      if not check_boundary(packages_in_truck, truck): return False
      if not check_overlap(packages_in_truck): return False
      if not check_support(packages_in_truck): return False
      if not check_fragile(packages_in_truck): return False
   return True