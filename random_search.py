__author__ = 'David T. Pocock'

import timeit
from operator import itemgetter
from genetic_algorithm import GeneticAlgorithm


class RandomSearch(GeneticAlgorithm):
    def __init__(self, target_string, solutions_size):
        self.target_string = target_string
        self.solutions_size = solutions_size

    def run(self):
        start_time = timeit.default_timer()
        solutions = self.generate_population(self.solutions_size)
        best_solution = self.evaluate(solutions)
        round_number = 0
        while self.target_string not in solutions:
            round_number += 1
            if best_solution[1] == 0:
                break
            new_solutions = self.generate_population(self.solutions_size)
            new_best_solution = self.evaluate(new_solutions)
            if new_best_solution[1] < best_solution[1]:
                solutions = new_solutions
                best_solution = new_best_solution
                print("\nFittest Value:", best_solution[1], "   Chromosome:", best_solution[0])
        print("\nThe task took {0:.2f} seconds".format(timeit.default_timer() - start_time))

    def evaluate(self, solutions):
        solutions_evaluated = []
        for solution_str in solutions:
            solution_fitness = self.fitness(solution_str, self.target_string)
            solution = solution_str, solution_fitness
            solutions_evaluated.append(solution)
        best_solution = min(solutions_evaluated, key=itemgetter(1))
        return best_solution
