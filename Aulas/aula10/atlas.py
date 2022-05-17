from bs4 import BeautifulSoup as BS
import requests

def getPagina(link):
    html = requests.get(link).text
    sopa = BS(html,"html5lib")

    divs = sopa.find_all("div","field-items")
    print(divs)
    
    return divs


def atlasAZ(atlas,letra):
    link = "https://www.atlasdasaude.pt"
    html = requests.get(link+'/doencasaaz/'+letra).text

    sopa = BS(html,"html5lib")

    for div_elem in sopa.find_all('div','views-row'):
        titulo = div_elem.findChildren(recursive=False)[0].h3.a
        ref = titulo["href"]
        
        descricao = div_elem.findChildren(recursive=False)[1].div.text.replace("\xa0","")

        atlas[titulo.text] = descricao #(descricao,getPagina(link+ref))


atlas={}

for letra in "abcdefghijklmnopqrstuvwxyz":
    atlasAZ(atlas,letra)


for key,value in atlas.items():
    print(f"{key} -> {value}\n")