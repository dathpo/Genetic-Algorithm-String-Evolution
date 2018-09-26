import random
import string

targetString = "Hello World!"
populationSize = 1000000

def generatePopulation(populationSize):
    population = []
    for i in range(0,populationSize):
        chromosome = []
        for char in range(0,12):
            char = random.choice(string.printable)
            chromosome.append(char)
        chromoString = ''.join(chromosome)
        population.append(chromoString)
    return population

def fitness(string, targetStr):
    if len(string) == len(targetStr):
        value = sum(el1 != el2 for el1, el2 in zip(string, targetStr))
        return value

"""def checkSimilarity(population targetString):
    targetString = [Hello World!]
    for chr in population:

"""

population = generatePopulation(populationSize)
for str in population:
    value = fitness(str, targetString)
    if value < 9:
        print (value, str)
