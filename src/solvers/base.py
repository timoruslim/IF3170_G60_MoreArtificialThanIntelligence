from ..engine.state import State
from ..engine.objective import ObjectiveFunction

class Result:
   def __init__(self, solver, objective, initial_state, final_state, objective_history, total_iterations, runtime, **metadata):
      self.solver = solver
      self.objective = objective
      self.initial_state = initial_state
      self.final_state = final_state
      self.objective_history = objective_history
      self.total_iterations = total_iterations
      self.runtime = runtime
      self.metadata = metadata

   def __str__(self):
      lines = []
      
      border = "=" * 100
      divider = "-" * 100
      
      lines.append(border)

      lines.append(f"Solver: {self.solver:}")
      lines.append(f"Objective Function: {self.objective:}")

      lines.append(divider)
      
      lines.append(f"Runtime: {self.runtime:.3f}s")
      lines.append(f"Total Iterations: {self.total_iterations:,}")
      
      if self.objective_history:
         init_score = self.objective_history[0]
         final_score = self.objective_history[-1]
         
         lines.append(f"Initial Objective: {init_score:.2f}")
         lines.append(f"Final Objective: {final_score:.2f}")
      
      if self.metadata:
         lines.append(divider)
         for key, value in self.metadata.items():
            formatted_key = key.replace('_', ' ').title()
            
            if isinstance(value, float):
               formatted_val = f"{value:.3f}"
            elif isinstance(value, list):
               if len(value) > 10: 
                  formatted_val = f"[{len(value)} values]"
               else: 
                  formatted_val = value
            else:
               formatted_val = str(value)
               
            lines.append(f"{formatted_key:<20} : {formatted_val}")
               
      lines.append(border)
      
      return "\n".join(lines)

   __repr__ = __str__

class Solver():
   def __init__(self, objective_function):
      self.objective = objective_function
   
   def solve(self, initial_state):
      raise NotImplementedError