
# Coded By :     Ali Suleman
# Email    :     alisulemanrajpar27@gmail.com
# LinkedIn :    https://www.linkedin.com/in/ali-suleman-a511942aa/

# Travelling Salesman Problem Using Genetic Algorithm
import random
INT_MAX = 2147483647
GENOTYPES = ""
POP_SIZE = int(input("Enter the population size: "))
MUT_RATE = float(input("Enter the Mutation Rate: "))
map = {
    'A'  : [('B',3),('C',6),('D',2)],
    'B'  : [('A',3),('C',4),('D',7)],
    'C'  : [('A',6),('B',4),('D',4)],
    'D'  : [('A',2),('B',7),('C',4)],
}
thresehold = int(input("Enter the threshold for convergence: "))
for key in map:
    GENOTYPES += key


# Genetic Algorithms TSP Problem
def hasConnection(src,dest,map):
    for index, adjacency in enumerate(map[src]):
        key = adjacency[0]
        if dest == key:
            return True, index
    return False, -1

def calculateFitness(string,map):
    #conditionValidation
    #Whether is path is possible or not.
    for i in range(len(string)-1):
        if not hasConnection(string[i],string[i+1],map)[0]:
            #print("Connect Fault")
            return INT_MAX
    fitnessValue = 0

    #Checking for Humiltonian Circuit (string[0] == string[len(string)-1])
    if not string[0] == string[-1]:
        #print("Hamiltonian Fault")
        return INT_MAX

    #Whether there is repition
    visited = []
    for i in range(len(string)-1):
        if string[i] not in visited:
            visited.append(string[i])
        else:
            #print("Repition Fault")
            return INT_MAX

    #If no repitiona and path ends with start
    for i in range(len(string)-1):
        fitnessValue += map[string[i]][hasConnection(string[i],string[i+1],map)[1]][1]
    return fitnessValue
    
        

def generatePopulation(population_size, chromo_len,start):
    global GENOTYPES
    global map
    population = []
    for i in range(population_size):
        Individual = []
        chromosome = []
        chromosome.append(start)
        while True:
            if len(chromosome) == chromo_len - 1:
                chromosome.append(start)
                break
            gene = random.choice(GENOTYPES)
            if gene not in chromosome:
                chromosome.append(gene)

        Individual.append(chromosome)
        Individual.append(calculateFitness(chromosome,map))
        population.append(Individual)
    return population


def selection(population):
    sorted_pop =sorted(population, key = lambda x: x[1])
    fiftyPercent = int(0.5 * POP_SIZE)
    return sorted_pop[:fiftyPercent]

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
        if random.random() < MUT_RATE:
            temp = chromosome[0][1]
            chromosome[0][1] = chromosome[0][3]
            chromosome[0][3]= temp
        chromosome[1] = calculateFitness(chromosome[0],map)
        mutated_offsprigs.append(chromosome)
    return mutated_offsprigs

def replacement(currPop, nextPopulation):
    for i in range(len(currPop)):
        if currPop[i][1] < nextPopulation[i][1]:
            nextPopulation[i][0] = currPop[i][0]
            nextPopulation[i][1] = currPop[i][1]
    return nextPopulation

########### MAIN CODE #####################
population = generatePopulation(POP_SIZE,len(map)+1,'A')
gen = 1
while gen < thresehold:
    print(f"\nGeneration {gen}: ")
    for idv in population:
        print(idv)
    population = sorted(population, key = lambda x: x[1])
    best_fits = selection(population)
    crossedOver = crossOver(best_fits,population)
    newGeneration = mutateGenes(crossedOver)
    population = replacement(population, newGeneration)
    print(f"{''.join(population[0][0])}\t\tGeneration : {gen}\t\tFitness : {population[0][1]}")
    gen += 1
