import time

print('=' * 12, ' SOMA DE ÍMPARES ', '=' * 12)
print('Escolha um número inicial e um final e mostrarei os números ímpares entre eles e a sua soma')
continua = 'S'
while continua == 'S':
    s = int(input('Número inicial: '))
    e = int(input('Número final: '))
    r = 0
    print('Os ímpares entre eles são: ')
    if s < e:
        print('CRESCENDO...')
        for c in range(s, e):
            if c % 2 == 1:
                print(c)
                r += c
        print('A soma destes números é: \n calculando...')
        time.sleep(1)
        print(r)
        continua = input('Mais uma vez? [s/n]').upper()
    else:
        print('DECRESCENDO...')
        for c in range(s, e - 1, -1):
            if c % 2 == 1:
                print(c)
                r += c
        print('A soma destes números é: \n calculando...')
        time.sleep(1)
        print(r)
        continua = input('Mais uma vez? [s/n]').upper()
print(' F I N I S H ')
