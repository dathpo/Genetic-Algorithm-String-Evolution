__author__ = 'David T. Pocock'


from hill_climbing import HillClimbing
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm("Hel", 1000, 0.8, 0.05)
    ga.run()
    hc = HillClimbing("Hel", 1000)
    hc.run()


if __name__ == "__main__":
    main()
