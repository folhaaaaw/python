from codigo72 import pessoa

pessoas = []

for i in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    pessoas.append( pessoa(nome,idade ))

pessoas[0].fazer_aniver()
print(pessoas[0].apresentar())

for p in pessoas:
    print(p)