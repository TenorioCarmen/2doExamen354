# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:12:51 2022

@author: PC
"""
import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 20)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def funcionobjetivo(individual):
    lista = individual
    iniciador=1
    suma=0
    lista.reverse()
    for i in lista:
        suma=suma+iniciador*i
        iniciador=iniciador*2
    return suma,

toolbox.register("evaluate", funcionobjetivo)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=False)

    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()
    #print(hof)
    #print(pop)
    print(log)
    print(hof)