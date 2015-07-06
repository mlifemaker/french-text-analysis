#-*- coding:utf-8 -*-
from nltk.corpus import stopwords

def tokenize(sentence):
    sw = set(stopwords.words('french'))
    output = [w for w in sentence.split() if w not in sw]
    return output

if '__main__' == __name__:
    input = "Véhicule très agréable a conduire, bonne tenue de route."
    res = tokenize(input)
    print res
