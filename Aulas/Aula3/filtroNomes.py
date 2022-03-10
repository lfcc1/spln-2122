import re
import pandas as pd

texto = open("ABM_807.txt", 'r').read()

listaNomes = []

# Registo de batismo n.º 53: João . Pai: João Rodrigues ; Mãe: Antónia Rosa         

nomesFemininos = pd.read_csv("NF.csv")
nomesMasculinos = pd.read_csv("NM.csv")

listaNomes += nomesMasculinos.NOME.tolist() + nomesFemininos.NOME.tolist()
# nomesMasculinos[nomesMasculinos]
print(len(listaNomes))

for n1,n2 in re.findall(r'\:\s*(.+)\s*c\.c\.\s*(.+)', texto):
    nomes = n1.split() + n2.split()
    for nome in nomes:
        if not re.match(r'[A-Z]', nome):
            continue
        else:
            if nome not in listaNomes:
                listaNomes.append(nome)

print(len(listaNomes))

for n1,n2,n3 in re.findall(r':\s*(.+) \s*\.\s*Pai:\s*(.+)\s*;\s*Mãe:\s*(.+)', texto):
    nomes = n1.split() + n2.split() + n3.split()
    for nome in nomes:
        if not re.match(r'[A-Z]', nome):
            continue
        else:
            if nome not in listaNomes:
                listaNomes.append(nome)

f = open("nomes.txt", "w")
for elem in listaNomes:
    f.write(elem + '\n')

f.close()



