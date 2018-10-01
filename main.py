__author__ = 'David T. Pocock'


from hill_climbing import HillClimbing
from random_search import RandomSearch
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm("Hello World!", 1400, 0.7, 0.04, True, 0.05, 0.65)
    ga.set_show_each_chromosome(False)
    ga.set_show_crossover_internals(False)
    ga.set_show_mutation_internals(False)
    ga.set_silent(True)
    ga.run(5)
    ga.get_stats()

    hc = HillClimbing("Hello World!", 10)
    hc.set_show_each_solution(False)
    hc.set_silent(True)
    hc.run(5)
    hc.get_stats()

    rs = RandomSearch("Hel", 1)
    rs.set_show_each_solution(False)
    rs.set_silent(True)
    rs.run(5)
    rs.get_stats()


if __name__ == "__main__":
    main()