import re

f = open('Git/spln-2122/Data/medicina.xml')
#print(f.read())
texto = f.read()

# 1
res = re.sub(r'.*?<page number="20"', '', texto, flags=re.S, count=1)
# 2
res = re.sub(r'<page number="544".*', '', res, flags=re.S, count=1)
# 3
res = re.sub(r'<text top="862" left="320" width="23" height="18" font="8">.*?</text>', '', res)
res = re.sub(r'<text top="862" left="324" width="15" height="18" font="8">.*?</text>', '', res)

res = re.sub(r'<text.*?>', '', res)
res = re.sub(r'</text>', '', res)
# 4 
res = re.sub(r'<[bi]>\s*</[bi]>','',res)
# 5
res = re.sub(r'<page.*?>','',res)
res = re.sub(r'</page>', '', res)

res = re.sub(r'V\nocabulario', '', res)

#Tratamento de entradas
def trataEntrada(entrada):
    #print('entrada:')
    #print(entrada)
    lista = re.split(r'</b>', entrada)
    if len(lista) >= 2:
        linha, resto = lista
        id = re.search(r'^(\d+)\s*(.*?)\s+(\w+)$',linha)
        if id:
            print(f"id={id[1]}")
            #+ id.group(1) + ", ga=" + id.group(2) + ", pos=" + id.group(3))
        else:
            print(linha,"?")
        # nome = re.findall(r'^\d+\s*(.*?)',linha)
        # print(id, nome)
    
    #print(linha1)
    #id = re.findall(r'(\d+)\s*(')

for elem in re.split(r'<b>',res):
    trataEntrada(elem)




#print(res)