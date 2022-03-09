import re
from itertools import chain

casamento_exp = re.compile(r"Registo de casamento n\.º \d+: ((?:\w+\s?)+)c\.c\. ((?:\w+\s?)+)")
batizado_exp = re.compile(r"Registo de bap?tismo n\.º \d+: ((?:\w+\s?)+)\. Pai: ((?:\w+\s?)+); Mãe: ((?:\w+\s?)+)")

with open("ABM_807.txt", encoding="UTF-8") as f:
    content = f.read()

casamentos : list[set[str]] = casamento_exp.findall(content)
batizados : list[set[str]] = batizado_exp.findall(content)

pessoas = list(chain.from_iterable(map(str.strip, p) for p in casamentos))

# KNOWN ISSUES: se duas pessoas casarem e batizarem uma criança ou se batizarem mais do que uma criança irão contar como pessoas diferentes
# alternativamente, se uma criança batizada entretanto casar, também vai contar como duas pessoas diferentes

last_name = lambda names: (names[-2] + ' ' if re.match(r"d(e|o|a)s?", names[-2]) else '') + names[-1]

for crianca, pai, mae in batizados:
    pai = pai.strip()
    mae = mae.strip()
    crianca = crianca.strip() + (' ' + last_name(mae.split()) if len(mae.split()) > 1 else '')\
                 + (' ' + last_name(pai.split()) if len(pai.split()) > 1 else '')
    pessoas.append(crianca)
    pessoas.append(mae)
    if pai.lower() != "incógnito": pessoas.append(pai)

counter = dict()
for pessoa in pessoas:
    counter.setdefault(pessoa, 0)
    counter[pessoa] += 1

print("**Nomes mais comuns**")
print(*[f"{x[0]}: {x[1]} pessoas" for x in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:10]], sep='\n')