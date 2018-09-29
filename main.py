import random, string, timeit
from operator import itemgetter


def target_string():
    return "Hello World!"


def population_size():
    return 1000


def available_chars():
    characters = string.ascii_letters + string.digits + ' ' + '\x7f' + string.punctuation
    return characters


def tournament_size():
    return int(0.2 * population_size())


def tournament_rounds():
    return population_size()


def strongest_winner_prob():
    return 0.75


def crossover_point():
    return 0.5


def crossover_rate():
    return 0.7


def mutation_rate():
    return 0.05


def main():
    start_time = timeit.default_timer()
    population = generate_population(population_size())
    if tournament_size() % 2 != 0:
        raise ValueError('Tournament Size must be an even number!')
    print("Hamming Distance     Chromosome")
    """for str in population:
        value = fitness(str, target_string())
        if value < 9:
            print("       {}            {}".format(value, str))"""
    winners = selection(population)
    check_for_crossover(winners)
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
    rand_int = random.random()
    return rand_int < probability


def tournament_selection(population):
    winners = []
    for t_round in range(0, tournament_rounds()):
        participants = []
        for participant_str in range(0, tournament_size()):
            random_index = random.randint(0, len(population) - 1)
            participant_str = population[random_index]
            participant_fitness = fitness(participant_str, target_string())
            participant = participant_str, participant_fitness
            participants.append(participant)
        if decision(strongest_winner_prob()):
            winner = min(participants, key=itemgetter(1))
            winners.append(winner)
        elif decision(strongest_winner_prob()):
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
    winners_strings = [str[0] for str in winners]
    paired_winners = list(zip(winners_strings[0::2], winners_strings[1::2]))
    return paired_winners


def check_for_crossover(parents):
    pre_mutation_next_gen = []
    for first_parent, second_parent in parents:
        if decision(crossover_rate()):
            binary_one_point_crossover(first_parent, second_parent)
        else:
            pre_mutation_next_gen.append(first_parent)
            pre_mutation_next_gen.append(second_parent)
            print(len(pre_mutation_next_gen))


def binary_one_point_crossover(first_parent, second_parent):
    print("First: ", first_parent, "Second: ", second_parent)
    first_parent_bit_array = []
    second_parent_bit_array = []
    i = 0
    for char_a, char_b in zip(first_parent, second_parent):
        print("char a: ", char_a, ", number: ", ord(char_a), ", bin: ", bin(ord(char_a)))
        print("char b: ", char_b, ", number: ", ord(char_b), ", bin: ", bin(ord(char_b)))
        i += 1
        point = int(round(crossover_point() * len(target_string())))
        binary_char_a = bin(ord(char_a))
        binary_char_b = bin(ord(char_b))
        if i <= point:
            first_parent_bit_array.append(binary_char_a)
            second_parent_bit_array.append(binary_char_b)
        else:
            first_parent_bit_array.append(binary_char_b)
            second_parent_bit_array.append(binary_char_a)
        #print(i)
    print(first_parent_bit_array)
    print(bit_array_to_string(first_parent_bit_array))
    print(second_parent_bit_array)
    print(bit_array_to_string(second_parent_bit_array))
    return 0


def bit_array_to_string(array):
    char_array = []
    for bit in array:
        char = chr(int(bit, 2))
        char_array.append(char)
    str = ''.join(char_array)
    print(str)


if __name__ == "__main__":
    main()
