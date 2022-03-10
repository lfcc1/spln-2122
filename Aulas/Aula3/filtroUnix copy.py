import re

f = open("ruasBraga_v1.txt", "r").read()

dicionarioNomes = set(nomes.strip() for nomes in open("nomes.txt", "r"))

# for elem in dicionarioNomes:
#     re.sub(elem, "#"+elem, f)

patern = "|".join(dicionarioNomes)

def fs(m):
    return f"@{m[1]}@" if m[1] in dicionarioNomes else m[1] 

f = re.sub(rf'\b([A-ZÂÁÉ]\w+)\b', fs, f)

f = re.sub(r"@\s*@", r" ", f)

f = re.sub(r"@\s*(da|do|das|dos|de)\s*@", r" \1 ", f)

print(f)