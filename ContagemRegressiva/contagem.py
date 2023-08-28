import time

print('-' * 12, ' CONTAGEM REGRESSIVA ', '-' * 12)
continua = 'S'
while continua == 'S':
    s = int(input('Digite o número maior: '))
    e = int(input('Agora digite o menor: '))
    p = int(input('De quanto em quanto desejas diminuir? '))
    if s < e:
        print('OPS! Digite para o primeiro número um valor maior que o segundo número.')
        continua = 'S'
    else:
        print('Agora vamos contar! \n ...')
        time.sleep(1)
        for c in range(s, e - 1, - p):
            print(c)
        print('PRONTO!')
        continua = input('Mais uma vez? [s/n] ').upper()
print('F I N I S H !')
