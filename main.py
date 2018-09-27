import random, string, timeit, operator
# from bitarray import bitarray


def target_string():
    return "Hello World!"


def population_size():
    return 1000


def available_chars():
    characters = string.ascii_letters + string.digits + ' ' + string.punctuation
    return characters


def tournament_size():
    return 2


def tournament_rounds():
    return 5


def main():
    start_time = timeit.default_timer()
    population = generate_population(population_size())
    print("Hamming Distance     Chromosome")
    for str in population:
        value = fitness(str, target_string())
        if value < 9:
            print("       {}            {}".format(value, str))
    print(selection(population))
    # print(crossover(0))
    print("\nThe process took {} seconds".format(timeit.default_timer() - start_time))


def generate_population(size):
    population = []
    for i in range(0,size):
        chromosome = []
        str_length = len(target_string())
        for char in range(0,str_length):
            if str_length != 12:
                print("Length: {}", str_length)
            char = random.choice(available_chars())
            chromosome.append(char)
        chromo_string = ''.join(chromosome)
        population.append(chromo_string)
    return population


def fitness(source, target):
    if len(source) == len(target):
        pairs = zip(source, target)
        hamming_distance = 0
        for a, b in pairs:
            if a != b:
                hamming_distance += 1
        return hamming_distance


def selection(population):
    return tournament_selection(population)


def tournament_selection(population):
    for rounds in range(0, tournament_rounds()):
        candidates = []
        for candidate in range(0, tournament_size()):
            random_index = random.randrange(len(population) - 1)
            candidate = population[random_index]
            cand_fitness = fitness(candidate, target_string())
            candidates.append(tuple(candidate, cand_fitness))
            print(candidate, random_index)
        print(candidates)
        winner = max(candidates, key=itemgetter(1))
        print(winner)


def decision(probability):
    return random.random() < probability


# def crossover(chromosome):
#     bit_array = bitarray(2**2)
#     return bit_array


if __name__ == "__main__":
    main()
