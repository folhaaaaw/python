nota= float(input('Nota:'))
freq = float(input('Freq: '))

if freq < 75:
    print('REPROVADO POR FALTA')
elif nota >= 7:
    print ('Aprovado')
elif nota >= 5:
    print ("AF")
else: print('dp')