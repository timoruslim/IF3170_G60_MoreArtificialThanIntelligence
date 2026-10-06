from .constraints import is_valid

class ObjectiveFunction:
   def evaluate(self, state):
      return 0.0

class MaxValueObjective(ObjectiveFunction):
   def __init__(self, penalty=-float('inf')):
      self.penalty = penalty

   def evaluate(self, state):
      if not is_valid(state):
         return self.penalty
      
      total_value = 0
      for truck in state.trucks:
         for package, _ in state.get_packages_in_truck(truck.id):
            total_value += package.value
      return total_value

class BonusObjective1(ObjectiveFunction):
   def evaluate(self, state):
      return 0.0

class BonusObjective2(ObjectiveFunction):
   def evaluate(self, state):
      return 0.0