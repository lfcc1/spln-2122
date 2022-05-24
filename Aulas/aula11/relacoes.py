import spacy
from re import *
texto = open("Harry_Potter_e_a_camara_dos_segredos.txt").read()


nlp = spacy.load("pt_core_news_lg")

texto = sub(r"\n{2,}","=", texto)
texto = sub(r"\n"," ", texto)
texto = sub(r"=","\n", texto)



for linha in split(r'\n',texto):
    for phrase in nlp(linha).sents:
        for ent in phrase.ents:
            print(ent.text, ent.label_)
