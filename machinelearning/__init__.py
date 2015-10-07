__author__ = 'Roy van den Hurk, Johan Munneke'

from random import randint
import Features
import random
import math
import operator

WEIGHT_MIN = 0
WEIGHT_MAX = 10


def individual(length, min, max):
    return [randint(min, max) for x in xrange(length)]


def population(count, length, min, max):
    return [individual(length, min, max) for x in xrange(count)]

def getAuthorValue(features):
    return (random.random - 0.5) * 2

def fitness(articles, weigths):
    p = {0: getAuthorValue}
    correct = 0
    for article in articles:
        sum = 0
        for i in range (1, len(weigths)):
            sum+= weigths[i] * p[i](article.features)
        if math.copysign(1,sum) == math.copysign(1,article.label):
            correct+=1
    return correct/(float)(len(articles))
    #sum(map(operator.mul, values, weights))

def evolve(pop, retain=0.2, random_select=0.5, mutate=0.01):
    sortedList = [ (fitness())]



if __name__ == '__main__':
    features = ['f1', 'f2', 'f3']
    # print population(10, len(features), WEIGHT_MIN, WEIGHT_MAX)
    # Test value extraction
    # print Features.getAuthorValue('dd')



