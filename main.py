__author__ = 'Roy van den Hurk, Johan Munneke'

from featureextraction.FeatureExtractor import FeatureExtractor
f = FeatureExtractor()
blob = "test test1 test2 test 3"
wordCount = f.test("test", blob)
print wordCount