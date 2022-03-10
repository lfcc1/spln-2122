import re

f = open("ruasBraga_v1.txt", "r").read()

dicionarioNomes = set(nomes.strip() for nomes in open("nomes.txt", "r"))

# for elem in dicionarioNomes:
#     re.sub(elem, "#"+elem, f)

patern = "|".join(dicionarioNomes)

f = re.sub(rf'\b({patern})\b', r"@\1@", f)

f = re.sub(r"@\s*@", r" ", f)

f = re.sub(r"@\s*(da|do|das|dos|de)\s*@", r" \1 ", f)

print(f)