from cmath import exp
import re
import nltk
from gensim.models import KeyedVectors
import gensim
import numpy as np
import networkx
import collections


f = open("noticia.txt").read()


def limpa(texto):
    stop = nltk.corpus.stopwords.words("portuguese")
    texto = re.sub(r"\[\d+\]", "", texto)
    expReg = ""
    for elem in stop:
        expReg += elem + "|"
    expReg = expReg.rstrip('|')
    texto = re.sub(fr"-?\b({expReg})\b", "", texto, flags=re.I)
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r",|'|\[|\]|\(|\)|\?|\"", "", texto)
    return texto

f = re.sub(r"\n+", " ", f)

f = nltk.sent_tokenize(f)
original = f.copy()

for i in range(len(f)):
    f[i] = limpa(f[i])
    if not f[i]:
        del (f[i])

model = KeyedVectors.load("model_300_20_sg.wv")

for i in range(len(f)):
    # print(f[i])
    f[i] = nltk.word_tokenize(f[i])
    del(f[i][-1])
    vetorPalavras = [model[x] for x in f[i] if x in model]
    f[i] = np.mean(vetorPalavras, axis = 0)

def my_similarity(vect1, vect2):
    return np.dot(vect1, vect2) / (np.linalg.norm(vect1) * np.linalg.norm(vect2))

matrix = np.zeros([len(f), len(f)])

for i in range(len(f)):
    for j in range(len(f)):
        matrix[i][j] = my_similarity(f[i],f[j])



graph = networkx.from_numpy_array(matrix)

score = networkx.pagerank(graph)

most_common = collections.Counter(score).most_common(5)
print(most_common)
frases = []
for elem in most_common:
    frases.append(elem[0])

frases.sort()

for elem in frases:
    print(original[elem])
    

# for elem in f:
#     print(elem)