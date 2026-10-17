from .base import Solver, Result
from ..engine.state import State, Placement
from ..engine.constraints import is_valid
from ..engine import get_random_neighbor
import random
import time


class GeneticAlgorithm(Solver):
    def __init__(self, objective, population_size=6, max_generations=100):
        super().__init__(objective)
        self.population_size = population_size
        self.max_generations = max_generations

    def _init_population(self, initial_state):
        return [
            State(initial_state.packages, initial_state.trucks, init="random_feasible")
            for i in range(self.population_size)
        ]

    def select(self, population, scores):
        min_score = min(scores)
        weights = [score - min_score for score in scores]
        if sum(weights) == 0:
            return random.choice(population)
        return random.choices(population, weights=weights, k=1)[0]

    def crossover(self, parent_a, parent_b):
        child = State(parent_a.packages, parent_a.trucks, init="outside")
        packages = list(parent_a.packages)
        if len(packages) <= 1:
            return parent_a.copy()
        crossover_point = random.randint(1, len(packages) - 1)
        for i, package in enumerate(packages):
            parent = parent_a if i < crossover_point else parent_b
            placement = parent.get_placement(package.id)
            if placement.truck_id is None:
                continue
            child.set_placement(package.id, placement.copy())
            if not is_valid(child):
                child.set_placement(package.id, Placement())
        return child

    def mutate(self, state):
        return get_random_neighbor(state)

    def solve(self, initial_state):
        population = self._init_population(initial_state)
        scores = [self.objective.evaluate(state) for state in population]
        best_index = scores.index(max(scores))
        best_state = population[best_index].copy()
        best_objective = scores[best_index]
        objective_history = [best_objective]
        average_history = [sum(scores) / len(scores)]
        start_time = time.perf_counter()
        for _ in range(self.max_generations):
            new_population = []
            while len(new_population) < self.population_size:
                parent_a = self.select(population, scores)
                parent_b = self.select(population, scores)
                child = self.crossover(parent_a, parent_b)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population
            scores = [self.objective.evaluate(state) for state in population]
            generation_best_index = scores.index(max(scores))
            generation_best = scores[generation_best_index]
            if generation_best > best_objective:
                best_objective = generation_best
                best_state = population[generation_best_index].copy()
            objective_history.append(best_objective)
            average_history.append(sum(scores) / len(scores))
        end_time = time.perf_counter()

        return Result(
            self.__class__.__name__,
            self.objective.__class__.__name__,
            initial_state,
            best_state,
            objective_history,
            self.max_generations,
            end_time - start_time,
            population_size=self.population_size,
            average_history=average_history,
            final_objective_value=best_objective,
        )