from ..engine.state import State
from ..engine.objective import ObjectiveFunction

class Result:
   def __init__(self, initial_state, final_state, objective_history, total_iterations, runtime, **metadata):
      self.initial_state = initial_state
      self.final_state = final_state
      self.objective_history = objective_history
      self.total_iterations = total_iterations
      self.runtime = runtime
      self.metadata = metadata

class Solver():
   def __init__(self, objective_function):
      self.objective = objective_function.evaluate
   
   def solve(self, initial_state):
      raise NotImplementedError