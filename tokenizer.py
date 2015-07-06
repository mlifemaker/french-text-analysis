#-*- coding:utf-8 -*-
from nltk.corpus import stopwords, wordnet as wn
import goslate

def tokenize(sentence):
    sw = set(stopwords.words('french'))
    output = [w for w in sentence.split() if w not in sw]
    return output

def similarity(term1, term2):
    gs = goslate.Goslate()
    term1_en = gs.translate(term1, 'en')
    term2_en = gs.translate(term2, 'en')
    print "translating %s to %s and %s to %s" %(term1, term1_en, term2, term2_en)
    s1 = wn.synsets(term1_en)[0]
    s2 = wn.synsets(term2_en)[0]
    res = s1.path_similarity(s2)
    return res
 
if '__main__' == __name__:
    input = "Véhicule très agréable a conduire, bonne tenue de route."
    res = tokenize(input)
    term1 = 'bateau'
    term2 = 'voile'
    sim = similarity(term1, term2)
    print sim
    
