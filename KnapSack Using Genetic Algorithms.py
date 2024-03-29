import random
objects = ['Bag','Rope','Knife','Torch','Bottle','Gulocose','Gold','Silver','Pot','Cash']
weights = [15,3,2,5,9,20,10,11,5,2]
survival_points = [15,7,10,5,8,17,30,10,13,11]
max_weight = 50
MUTATION_RATE = 0.1

def fitenessVal(chromosome):
    wt = 0
    sp = 0
    for i in range(len(chromosome)):
        wt = wt + (chromosome[i] * weights[i])
        sp = sp + (chromosome[i] * survival_points[i])
    
    if wt > max_weight:
        return 0
    else:
        return sp
    
def generatePopulation(size,string_length):
    population = []
    for i in range(size):
        individual = []
        chromosome = []
        for j in range(string_length):
            chromosome.append(random.randint(0,1))
        individual.append(chromosome)
        individual.append(fitenessVal(chromosome))
        population.append(individual)
    return population


def selection(population):
    sorted_population = sorted(population,key=lambda x:x[1],reverse=True)
    ratio = int(0.5*len(sorted_population))
    return sorted_population[:ratio]

def crossover(selected_pop):
    newPopulation = []
    for i in range(len(selected_pop)):
        parent1 = selected_pop[i][0]
    
        # Avoiding Mating of Parent With Itself
        tempPop = [x for x in selected_pop]
        for index, individual in enumerate(tempPop):
            if individual[0] == parent1:
                tempPop.pop(index)
                break

        parent2 = random.choice(tempPop)[0]
        crossoverPoint = random.randint(1,len(parent1)-1)
        child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
        child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]
        individual1 = []
        individual2 = []
        individual1.append(child1)
        individual1.append(fitenessVal(child1))
        individual2.append(child2)
        individual2.append(fitenessVal(child2))
        newPopulation.append(individual1)
        newPopulation.append(individual2)
    return newPopulation

def invert(bit):
    if bit == 0:
        return 1
    else:
        return 0

def mutate(offsprings):
    mutated = []
    for offspring in offsprings:
        for i in range(len(offspring[0])):
            if random.random() < MUTATION_RATE:
                offspring[0][i] = invert(offspring[0][i])
                offspring[1] = fitenessVal(offspring[0])
        mutated.append(offspring)
    return mutated
        
def displayPopulation(population,string):
    print(f"\n{string}")
    for individual in population:
        print(individual)

def k_test_convergence(populationMax,k):
    m = 1
    while m < k:
        if populationMax[-m] != populationMax[-m-1]:
            return False
        m += 1
    return True
        
gen = 1
population = generatePopulation(10,len(objects))
k = 10
populationMax = []


while True:
    selected = selection(population)
    crossedOver = crossover(selected)
    mutated = mutate(crossedOver)
    population = sorted(mutated,key=lambda x:x[1],reverse=True)
    print(f"{population[0][0]}\t\tGeneration : {gen}\t\tFitness : {population[0][1]}")
    populationMax.append(population[0][1])
    if gen >= k and k_test_convergence(populationMax,k):
        print("CONVERGED")
        break
    gen = gen + 1




