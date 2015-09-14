import math
from textblob import TextBlob as tb

__author__ = 'Roy van den Hurk, Johan Munneke'


class FeatureExtractor:
    def __init__(self):
        pass

    def test(self, word, blob):
        return tb(blob).words.count(word)