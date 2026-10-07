from .base import Solver

class SimulatedAnnealing(Solver):
   def __init__(self, objective, initial_temp, cooling_rate, min_temp, max_iterations):
      super().__init__(objective)
      self.initial_temp = initial_temp
      self.cooling_rate = cooling_rate
      self.min_temp = min_temp
      self.max_iterations = max_iterations

   def solve(self, initial_state):
      current_state = initial_state
      current_objective = self.objective.evaluate(current_state)

      return 