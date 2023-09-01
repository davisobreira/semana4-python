import time

print('-' * 12, ' TABUADA 2.0 ', '-' * 12)
continua = 'S'
while continua == 'S':
    option = input('ESCOLHA:\n [M] Multiplicação\n [D] Divisão \n').upper()
    match option:
        case 'M':

            print('*' * 12, ' MULTIPLICAÇÃO ', '*' * 12)
            n = int(input('Escolha um número para multiplicar: '))
            s = int(input('Escolha um número para ser o multiplicador inicial: '))
            e = int(input('Escolha um número para ser o multiplicador final: '))

            if s > e:
                print('Calculando em forma decrescente\n ...')
                time.sleep(1)
                for c in range(s, e - 1, -1):
                    r = n * s
                    print(f'{n} X {s} = {r}')
                    s = s - 1
                continua = input('Calcular mais uma vez? [s/n]').upper()
            else:
                print('Calculando em forma crescente\n ...')
                time.sleep(1)
                for c in range(s, e + 1):
                    r = n * s
                    print(f'{n} X {s} = {r}')
                    s = s + 1
                continua = input('Calcular mais uma vez? [s/n]').upper()
        case 'D':

            print('*' * 12, ' DIVISÃO ', '*' * 12)
            n = int(input('Escolha um número para ser o dividendo: '))
            s = int(input('Escolha um número para ser o divisor inicial: '))
            e = int(input('Escolha um número para ser o divisor final: '))

            if s > e:
                print('Calculando em forma decrescente\n ...')
                time.sleep(1)
                for c in range(s, e - 1, - 1):
                    r = n / s
                    print(f'{n} / {s} = {r:,.2f}')
                    s = s - 1
                continua = input('Calcular mais uma vez? [s/n]').upper()
            else:
                print('Calculando em forma crescente\n ...')
                time.sleep(1)
                for c in range(s, e + 1):
                    r = n / s
                    print(f'{n} / {s} = {r:,.2f}')
                    s = s + 1
                continua = input('Calcular mais uma vez? [s/n]').upper()
print('-' * 12, ' F I N I S H ', '-' * 12)
