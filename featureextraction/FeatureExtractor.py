import datetime
import math
from xml.etree import ElementTree

from textblob import TextBlob


DATABASE_URL = 'data/articles.db'


class FeatureExtractor:
    def __init__(self):
        self.articles = []
        self.blobs = []  # TODO: create blobs

    def set_training_data(self, articles):
        self.articles = articles
        self.blobs = []
        for article in articles:
            self.blobs.append(self.clean_html(article.html))

    def get_features(self, article):
        features = Features()
        # features.article = article
        # features.author = article.author
        # features.date = article.date
        features.tf_idf = {}
        blob = TextBlob(self.clean_html(article.html))
        for word in blob.words:
            features.tf_idf[word] = self.get_tf_idf(blob, word)
        return features

    def get_tf_idf(self, blob, word):
        return self.tf(blob, word) * self.idf(word)

    def tf(self, blob, word):
        return blob.words.count(word)

    def idf(self, word):
        return 1 + math.log(len(self.blobs) / float((1 + self.n_containing(word, self.blobs))))

    def n_containing(self, word, bloblist):
        return sum(1 for blob in bloblist if word in blob)

    def clean_html(self, html):
        return ''.join(ElementTree.fromstring(html).itertext())


class Article:
    def __init__(self):
        self.html = ''
        self.author = ''
        self.date = datetime.datetime(1, 1, 1)
        self.title = ''

    def from_sql(self, index):
        # TODO: query database
        pass


class Features:
    def __init__(self):
        self.tf_idf = None
        pass