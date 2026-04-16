carrinho = ['notebook','mouse','teclado']

for item in carrinho:
    print(item)
    
carrinho.append('Headset')
carrinho.remove('mouse')
carrinho.insert(1,'impressora')
carrinho[0] = 'mac'
carrinho.sort() 
print(carrinho)
