maior = None

for i in range(5):
    n = int(input('Digite> '))
    if maior is None or n > maior:
        maior = n
        

    print(f'O maior é {maior}')
    