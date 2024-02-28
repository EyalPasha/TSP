import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def fitness(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]


def mutate(route):
    mutation_point1, mutation_point2 = random.sample(range(len(route)), 2)
    route[mutation_point1], route[mutation_point2] = route[mutation_point2], route[mutation_point1]
    return route


def solve(points):
    population_size, generations = 100, 1000
    population = [random.sample(points, len(points)) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        elite_size = int(0.1 * population_size)
        elite = population[:elite_size]
        children = [crossover(random.choice(elite), random.choice(elite)) for _ in range(population_size - elite_size)]
        population = elite + [mutate(child) if random.random() < 0.1 else child for child in children]

    return population[0]
