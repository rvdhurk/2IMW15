__author__ = 'Roy van den Hurk, Johan Munneke'


from featureextraction import *
from pprint import pprint

articles = Article.from_sql()
featureExtractor = FeatureExtractor()
featureExtractor.set_training_data(articles)
print 'Done loading articles'
for article in articles:
    features = featureExtractor.get_features(article)
    pprint (vars(features))
    print 'Extracted features'
print 'Done'