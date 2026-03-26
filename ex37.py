def faixa_etaria(idade):
    if idade <= 0:
        return 'Idade invalidada'
 
    elif idade < 12: 
        return "Criança"
    elif idade < 17:
        return 'adolescente'
    else: 
        return 'Adulto'
    
    
while True:
     idade = input('Digite a idade ou SAIR')  
     if idade.lower() == 'sair':
         break 
     print(faixa_etaria(int(idade)))
     
     print('Até mais...')
     