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
    return int(0.05 * population_size())


def tournament_rounds():
    return population_size()


def strongest_winner_prob():
    return 0.65


def crossover_point():
    return random.random()


def crossover_rate():
    return 0.8


def mutation_rate():
    return 0.05


def set_mutation_rate(rate):
    return rate


def main():
    start_time = timeit.default_timer()
    population = generate_population(population_size())
    if tournament_size() % 2 != 0:
        raise ValueError('Tournament Size must be an even number!')
    generation_number = 0
    print("Hamming Distance      Chromosome          Generation")
    while target_string() not in population:
        generation_number += 1
        winners = selection(population)
        pre_mutation_generation = check_for_crossover(winners)
        new_generation = mutate(pre_mutation_generation)
        population = new_generation
        counter = 0
        for chromosome in population:
            counter += 1
            fit_value = fitness(chromosome, target_string())
            if counter == 1:
                fittest_chromosome = chromosome, fit_value
            print("       {}            {}            {}".format(str(fit_value).rjust(2), chromosome.rjust(2), generation_number).rjust(2))
            if fit_value < fittest_chromosome[1]:
                fittest_chromosome = chromosome, fit_value
                if fit_value == 0:
                    break
        print("\nFittest Value:", fittest_chromosome[1], "   Chromosome:", fittest_chromosome[0], "\n")
    print("The process took {} seconds".format(timeit.default_timer() - start_time))


def generate_population(size):
    population = []
    for i in range(0,size):
        chromosome = []
        str_length = len(target_string())
        for char in range(0,str_length):
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
    new_generation = []
    for first_parent, second_parent in parents:
        if decision(crossover_rate()):
            children_duo = binary_one_point_crossover(first_parent, second_parent)
            #print("Children duo:", children_duo)
            for child in children_duo:
                new_generation.append(child)
        else:
            new_generation.append(first_parent)
            new_generation.append(second_parent)
    return new_generation


def binary_one_point_crossover(first_parent, second_parent):
    #print("First parent:", first_parent, "Second parent:", second_parent)
    first_child_char_array = []
    second_child_char_array = []
    i = 0
    for char_a, char_b in zip(first_parent, second_parent):
        #print("char a:", char_a, ", number:", ord(char_a), ", bin:", bin(ord(char_a)))
        #print("char b:", char_b, ", number:", ord(char_b), ", bin:", bin(ord(char_b)))
        i += 1
        point = int(round(crossover_point() * len(target_string())))
        if i <= point:
            first_child_char_array.append(char_a)
            second_child_char_array.append(char_b)
        else:
            first_child_char_array.append(char_b)
            second_child_char_array.append(char_a)
    first_child = ''.join(first_child_char_array)
    second_child = ''.join(second_child_char_array)
    return first_child, second_child


def mutate(generation):
    new_generation = []
    for chromosome in generation:
        #print("Chromosome:", chromosome, "\n")
        chromosome_bit_array = []
        for char in chromosome:
            binary_char = bin(ord(char))
            #print("Char:", char, " Number:", ord(char), " Binary Char:", binary_char)
            new_binary_char_array = ['0', 'b', '1']
            for bit in binary_char[3:]:
                if decision(mutation_rate()):
                    flipped_bit = int(bit) ^ 1
                    #print("Bit:", str(bit), " Flipped bit:", str(flipped_bit))
                    new_binary_char_array.append(str(flipped_bit))
                else:
                    #print("Bit:", str(bit))
                    new_binary_char_array.append(str(bit))
            new_binary_char = ''.join(new_binary_char_array)
            #print("New Char:", chr(int(new_binary_char, 2)), " Number:", int(new_binary_char, 2), " Binary Char:", new_binary_char, "\n")
            chromosome_bit_array.append(new_binary_char)
        #print("New Chromosome Bit Array:", chromosome_bit_array)
        new_chromosome = bit_array_to_string(chromosome_bit_array)
        #print("Previous Chromosome:", chromosome, " New Chromosome:", new_chromosome, "\n")
        new_generation.append(new_chromosome)
    return new_generation


def bit_array_to_string(array):
    char_array = []
    for bit in array:
        char = chr(int(bit, 2))
        char_array.append(char)
    str = ''.join(char_array)
    return str


if __name__ == "__main__":
    main()
