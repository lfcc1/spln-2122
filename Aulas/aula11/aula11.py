import spacy
from re import *

nlp = spacy.load("pt_core_news_lg")

texto = open("Tolstoi-O_prisioneiro_do_Caucaso.txt").read()
texto = sub(r"\n{2,}","=", texto)
texto = sub(r"\n"," ", texto)
texto = sub(r"=","\n", texto)
#print(texto)


for linha in split(r'\n',texto):
    for phrase in nlp(linha).sents:
        n = 1
        state = 0
        for token in phrase:

            if state == 0:
                if token.ent_iob_ == "B":
                    name = token.text
                    state = 1
                    pos = token.pos_
                    ent_type = token.ent_type_
                else:
                    print(n , token.text, token.lemma_, token.pos_, token.ent_type_, token.morph, sep="\t")
            elif state == 1:
                if token.ent_iob_ == "I":
                    name += "_" + token.text
                elif token.ent_iob_ == "O":
                    print(n, name, name, pos, ent_type, sep ="\t")
                    print(n , token.text, token.lemma_, token.pos_, token.ent_type_, token.morph, sep="\t")
                    state = 0
                elif token.ent_iob_ == "B":
                    print(n, name, name, pos, ent_type, sep ="\t")
                    name = token.text
                    state = 1
                    pos = token.pos_
                    ent_type = token.ent_type_    
            n = n + 1
        if state == 1:
             print(n, name, name, pos, ent_type, sep ="\t")
        print()
