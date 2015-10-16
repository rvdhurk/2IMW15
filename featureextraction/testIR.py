__author__ = 'Roy van den Hurk, Johan Munneke'

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import TweetTokenizer


test = 'this is a test \'string\' where the stop can\'t words should be removed, also we want to use synonyms to get a better result.'

stop = stopwords.words('english')

tokenizer = RegexpTokenizer(r'\w+')
result1 = ([i for i in tokenizer.tokenize(test)])
print result1

tokenizer2 = TweetTokenizer()
result12 = ([i for i in tokenizer.tokenize(test)])
print result12

result2 = ([i for i in result1 if i not in stop])
print result2

st1 = LancasterStemmer()
result3 = ([st1.stem(i) for i in result2])
print result3

st2 = EnglishStemmer()
result4 = ([st2.stem(i) for i in result2])
print result4

st3 = WordNetLemmatizer()
result5 = ([st3.lemmatize(i) for i in result2])
print result5

st4 = PorterStemmer()
result6 = ([st4.stem(i) for i in result2])
print result6