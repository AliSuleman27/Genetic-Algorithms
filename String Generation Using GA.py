
# Coded By :     Ali Suleman
# Email    :     alisulemanrajpar27@gmail.com
# LinkedIn :    https://www.linkedin.com/in/ali-suleman-a511942aa/
# Genetic Algorithms - String Generation

import random
def calculateFitness(chromosome):
    global TARGET_STRING
    fitness = 0
    for i in range(len(TARGET_STRING)):
        if chromosome[i] != TARGET_STRING[i]:
            fitness += 1
    return fitness

def generatePopulation(population_size, length):
    global GENOTYPES
    population = []
    for i in range(population_size):
        individual = []
        chromosome = []
        for j in range(length):
            gene = random.choice(GENOTYPES)
            chromosome.append(gene)
        fitnessValue = calculateFitness(chromosome)
        individual.append(chromosome)
        individual.append(fitnessValue)
        population.append(individual)
    return population

def selection(population):
    sorted_population = sorted(population,key=lambda x:x[1])
    fiftyPrecent = int(0.5*POP_SIZE)
    return sorted_population[:fiftyPrecent]

def crossOver(fit_indviduals, population):
    offsprings_crossovered = []
    for i in range(POP_SIZE):
        parent1 = random.choice(fit_indviduals)[0]
        parent2 = random.choice(population[:(50*POP_SIZE)])[0]
        #using single point crossover
        crossOverPoint = random.randint(1,len(parent1))
        crossoveredChild = parent1[:crossOverPoint] + parent2[crossOverPoint:]
        offsprings_crossovered.extend([[crossoveredChild]])
        offsprings_crossovered[len(offsprings_crossovered)-1].append(-1)
    return offsprings_crossovered


def mutateGenes(offsprings):
    mutated_offsprigs = []
    for chromosome in offsprings:
        for i in range(len(chromosome[0])):
            if random.random() < MUTATION_RATE:
                chromosome[0][i] = random.choice(GENOTYPES)
        chromosome[1] = calculateFitness(chromosome[0])
        mutated_offsprigs.append(chromosome)
    return mutated_offsprigs

def replacement(currPop, nextPopulation):
    for i in range(len(currPop)):
        if currPop[i][1] < nextPopulation[i][1]:
            nextPopulation[i][0] = currPop[i][0]
            nextPopulation[i][1] = currPop[i][1]
    return nextPopulation

def printIt(array,limit):
    for index, node in enumerate(array):
        print(node)
        if index == limit:
            return


GENOTYPES = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,'
MUTATION_RATE = 0.1
print("Enter the Size for Every Generation: ")
POP_SIZE = int(input())

print("Enter teh Target String you want to generate Acceptable (A-Z / a-z / 0-9): ")
TARGET_STRING = input()

gen = 1
length = len(TARGET_STRING)
population = generatePopulation(POP_SIZE,length)

while True:
    population = sorted(population,key = lambda x:x[1])
    best_fit = selection(population)
    crossOvered = crossOver(best_fit,population)
    newGeneration = mutateGenes(crossOvered)

    population = replacement(population, newGeneration)
    population = sorted(population,key = lambda x: x[1])
    print(f"{''.join(population[0][0])}\t\tGeneration : {gen}\t\tFitness : {population[0][1]}")
    # convergence test
    if population[0][1] == 0:
        print("Target Found .....")
        print(f"{''.join(population[0][0])}\t\tGeneration : {gen}\t\tFitness : {population[0][1]}")
        break
    else:
        gen += 1
