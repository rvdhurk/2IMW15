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
article.publisher = 'aaaaaaa'

articles = []
for i in range(0, 10):
    articles.append(article)

featureExtractor = FeatureExtractor()
featureExtractor.set_training_data(articles)

features = featureExtractor.get_features(article)

print '<======= Features =======>'
print 'tf/idf (html) =>'
print '\n'.join('\t{}: {}'.format(k, v) for k, v in features.tf_idf.items())
print 'author =>'
print '\t' + features.author
print 'date =>'
print '\t', features.date
print 'title =>'
print '\t' + features.title
print 'length =>'
print '\t', features.length
print 'publisher =>'
print '\t' + features.publisher