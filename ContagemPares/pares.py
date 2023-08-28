import time

print('+' * 12, ' CONTAGEM DE PARES ', '+' * 12)
continua = 'S'
while continua == 'S':
    print('Escolha um número inicial e um final e mostrarei os números pares entre eles.')
    s = int(input('Número inicial: '))
    e = int(input('Número final: '))
    if s < e:
        print('Vamos contar crescendo! \n ...')
        time.sleep(1)
        for c in range(s, e + 1, 1):
            if c % 2 == 0:
                print(c)
        continua = input('Continuar [s/n]').upper()
    else:
        print('Vamos contar decrescendo! \n ...')
        time.sleep(1)
        for c in range(s, e - 1, -1):
            if c % 2 == 0:
                print(c)
        continua = input('Continuar [s/n]').upper()
print('PRONTO')
