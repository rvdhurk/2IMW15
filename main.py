__author__ = 'Roy van den Hurk, Johan Munneke'

import datetime

from featureextraction import *


article = Article()
article.author = "test author"
article.date = datetime.datetime(1, 1, 1)
article.html = '<head>' \
               '<body>' \
               ' test  <h1> aaa </h1> <a> aaaaaaa </a> test </body>' \
               '</head>'
article.title = 'test'

articles = []
for i in range(0, 10):
    articles.append(article)

featureExtractor = FeatureExtractor()
featureExtractor.set_training_data(articles)

features = featureExtractor.get_features(article)
print features.tf_idf