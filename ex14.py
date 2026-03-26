soma = 0
cont = 0

while True: 
    n = int(input('Digite n:'))
    if n == 0:
        break
    soma += n      #equivalente soma = soma + n 
    cont += 1 
    
    if cont > 0: 
        print(f'Media{soma / cont}')
    else:
        print('sem media')
        