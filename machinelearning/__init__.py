__author__ = 'Roy van den Hurk, Johan Munneke'

from random import randint
import Features

WEIGHT_MIN = 0
WEIGHT_MAX = 10


def individual(length, min, max):
    return [randint(min, max) for x in xrange(length)]


def population(count, length, min, max):
    return [individual(length, min, max) for x in xrange(count)]


def fitness(weights):
    pass


if __name__ == '__main__':
    features = ['f1', 'f2', 'f3']
    # print population(10, len(features), WEIGHT_MIN, WEIGHT_MAX)
    # Test value extraction
    # print Features.getAuthorValue('dd')


