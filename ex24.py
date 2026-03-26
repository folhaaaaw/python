num = int(input('Tabuada: '))

for i in range(1,11):
    print(f'{num} x {i} = {num * i}')
    
    print('*' * 50)
    print('TABUADA COMPLETA')
    print('*' * 50)
    for i in range(1,11):
        for j in range(11):
            print(f'{i} x {j} = {j * i}')
        print('*' * 50)
            