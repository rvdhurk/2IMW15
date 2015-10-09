__author__ = 'Roy van den Hurk, Johan Munneke'

from random import randint, uniform
import Features
import random
from faker import Factory
from featureextraction import Article

WEIGHT_MIN = 0
WEIGHT_MAX = 10


def individual(length, min, max):
    return [uniform(min, max) for x in xrange(length)]


def population(count, length, min, max):
    return [individual(length, min, max) for x in xrange(count)]


def getAuthorValue(features):
    return (random.random() - 0.5) * 2


def fitness(articles, weigths):
    p = {0: getAuthorValue, 1: getAuthorValue}
    correct = 0
    for article in articles:
        sum = 0
        for i in range(1, len(weigths)):
            print article.features
            sum += weigths[i] * p[i](article.features)
        if article.label == 0:
            if -0.1 <= sum <= 0.1:
                correct += 1
        elif sum > 0.1 and article.label == 1:
            correct += 1
        elif sum < -0.1 and article.label == -1:
            correct += 1
    return correct / (float)(len(articles))


def evolve(articles, pop, retain=0.2, random_select=0.5, mutate=0.01):
    sortedList = [(fitness(articles, x), x) for x in pop]
    sortedList = [x[1] for x in sorted(sortedList, reverse=True)]
    retain_length = int(len(sortedList) * retain)
    parentList = sortedList[:retain_length]

    for individual in sortedList[retain_length:]:
        if random_select > random.random():
            parentList.append(individual)

    for individual in parentList:
        if mutate > random.random():
            featureToMutate = randint(0, len(individual) - 1)
            individual[featureToMutate] = uniform(min(individual), max(individual))

    parentListLength = len(parentList)
    desiredParentListLength = len(pop) - parentListLength
    children = []
    while len(children) < desiredParentListLength:
        male = randint(0, parentListLength - 1)
        female = randint(0, parentListLength - 1)
        if male != female:
            children.append(mutator(male, female, parentList))
    parentList.extend(children)
    return parentList


def mutator(male, female, parentList):
    male = parentList[male]
    female = parentList[female]
    half = len(male) / 2
    child = male[:half] + female[half:]
    return child


def grade(articles, pop):
    summed = sum(fitness(articles, x) for x in pop)
    return summed / float(len(pop))


if __name__ == '__main__':
    articles = []
    fake = Factory.create()
    for i in range(0, 100):
        article = Article(i, fake.name(), fake.name(), fake.date(), fake.name(), fake.text(), fake.name(),
                          randint(-1, 1))
        articles.append(article)
    p = population(100, 2, 0, 100)
    for x in xrange(100):
        p = evolve(articles, p)
        # print grade(articles, p)

        # print population(10, len(features), WEIGHT_MIN, WEIGHT_MAX)
        # Test value extraction
        # print Features.getAuthorValue('dd')



