from .base import Solver, Result
from ..engine import *
import math
import random
import time

class Schedule():
   def __init__(self, initial_temperature):
      self.initial_temperature = initial_temperature

   def __call__(self, t):
      raise NotImplementedError

# See https://lemoine-or.github.io/MetaheuristicsPlatform/components/simulated-annealing-cooling-schedules.html?utm_source=chatgpt.com

class GeometricSchedule(Schedule):
   def __init__(self, initial_temperature, alpha):
      super().__init__(initial_temperature)
      self.alpha = alpha

   def __call__(self, t):
      return self.initial_temperature * self.alpha ** t

class LinearSchedule(Schedule):
   def __init__(self, initial_temperature, beta):
      super().__init__(initial_temperature)
      self.beta = beta

   def __call__(self, t):
      return self.initial_temperature - self.beta * t

class RationalSchedule(Schedule):
   def __init__(self, initial_temperature, beta):
      super().__init__(initial_temperature)
      self.beta = beta

   def __call__(self, t):
      return self.initial_temperature / (1 + self.beta * self.initial_temperature * t)

class LogarithmicSchedule(Schedule):
   def __init__(self, initial_temperature, c=math.log(2), t0=2):
      super().__init__(initial_temperature)
      self.c = c
      self.t0 = t0

   def __call__(self, t):
      return self.initial_temperature * self.c / math.log(t + self.t0)   

class SimulatedAnnealing(Solver):
   def __init__(self, objective, schedule, minimum_temperature=1e-8, max_iterations=10000):
      super().__init__(objective)
      self.schedule = schedule
      self.minimum_temperature = minimum_temperature
      self.max_iterations = max_iterations

   def solve(self, initial_state):
      current_state = initial_state

      t = 0
      objective_history = [self.objective(current_state)]
      probability_history = []

      start_time = time.perf_counter()
      
      for t in range(1, self.max_iterations + 1):
         T = self.schedule(t)
         if T <= self.minimum_temperature:
            break

         next_state = get_random_neighbor(current_state)
         dE = self.objective(next_state) - self.objective(current_state)
         p = 1.0 if dE > 0 else math.exp(dE / T)

         if random.random() < p:
            current_state = next_state

         objective_history.append(self.objective(current_state))
         probability_history.append(p)

      end_time = time.perf_counter()

      return Result(
         initial_state, 
         current_state, 
         objective_history, 
         t, 
         end_time - start_time, 
         probability_history=probability_history
      )