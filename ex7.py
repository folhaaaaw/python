opc = int(input('1- cad \n2-alt \n3-exc \n4-sair'))

match opc: 
    case 1:
        print('Cadastrar')
    case 2:
        print('alterar')
    case 3:
        print('excluir')
    case 4:
        print('sair')
    case _ :
        print('valor errado')