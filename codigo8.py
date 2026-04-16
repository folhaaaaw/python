from codigo82 import Pilha

def validar_exp(expressao):
    pilha = Pilha()
    
    #(5+6)*(6-9)
    for c in expressao:
        if c == '(':
            pilha.push(c)
        elif c == ')':
            if pilha.vazia():
                return False
                pilha.pop()
            return pilha.vazia()