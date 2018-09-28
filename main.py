import random, string, timeit
from operator import itemgetter


def target_string():
    return "Hello World!"


def population_size():
    return 1000


def available_chars():
    characters = string.ascii_letters + string.digits + ' ' + string.punctuation
    return characters


def tournament_size():
    return int(0.2 * population_size())


def tournament_rounds():
    return population_size()


def probability():
    return 0.75


def crossover_rate():
    return 0.7


def mutation_rate():
    return 0.05


def main():
    start_time = timeit.default_timer()
    population = generate_population(population_size())
    print("Hamming Distance     Chromosome")
    """for str in population:
        value = fitness(str, target_string())
        if value < 9:
            print("       {}            {}".format(value, str))"""
    winners = selection(population)
    winners_strings = [str[0] for str in winners]
    crossover(winners_strings[0], 'test')
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


def decision(probability):
    int = random.random()
    return int < probability


def tournament_selection(population):
    winners = []
    for round in range(0, tournament_rounds()):
        participants = []
        for participant_str in range(0, tournament_size()):
            random_index = random.randint(0, len(population) - 1)
            participant_str = population[random_index]
            participant_fitness = fitness(participant_str, target_string())
            participant = participant_str, participant_fitness
            participants.append(participant)
        if decision(probability()):
            winner = min(participants, key=itemgetter(1))
            winners.append(winner)
        elif decision(0.75):
            temp_participant = min(participants, key=itemgetter(1))
            participants.remove(temp_participant)
            winner = min(participants, key=itemgetter(1))
            winners.append(winner)
            participants.append(temp_participant)
        else:
            first_temp_participant = min(participants, key=itemgetter(1))
            participants.remove(first_temp_participant)
            second_temp_participant = min(participants, key=itemgetter(1))
            participants.remove(second_temp_participant)
            winner = min(participants, key=itemgetter(1))
            winners.append(winner)
            participants.append(first_temp_participant)
            participants.append(second_temp_participant)
    return winners


def crossover(first_chromosome, second_chromosome):
    print(first_chromosome)
    for char in first_chromosome:
        print("char: ", char, ", number: ", ord(char), ", bin: ", bin(ord(char)))
        bin(ord(char))
        print(chr(127), "  ", repr(chr(127)))
        print(len(available_chars()))
    #print(result)
    return 0


if __name__ == "__main__":
    main()
