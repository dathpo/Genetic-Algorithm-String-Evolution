__author__ = 'David T. Pocock'


from hill_climbing import HillClimbing
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm("Hello World!", 1000, 0.8, 0.05)
    ga.run()
    hc = HillClimbing("Hello World!")
    hc.get_target_string()


if __name__ == "__main__":
    main()
