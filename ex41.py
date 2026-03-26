def validar(frase):
    return frase != ''

arq = open('dados.txt','w',encoding='utf-8')

while True:
    frase = input('digite algo: ')
    if frase.lower() == 'sair':
        break 
    if validar(frase) == False:
        print('Frase errada')
        continue
    arq.write(frase + '\n')
arq.close()
    