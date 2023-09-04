import time

print('/' * 12, ' PROGRESSÃO ARITMÉTICA ', '/' * 12)
continua = 'S'
while continua == 'S':
    print('Escolha o primeiro e o segundo termo de uma sequência. \n')
    n1 = int(input('Primeiro termo: '))
    n2 = int(input('Segundo termo: '))
    r = int(n2 - n1)
    if r == 0:
        d = 'constante'
        print(f'A razão entre esses números é: {r}, portanto esta progressão aritmética é: {d}.')
        print(f'Portanto qualquer posição será igual a: {n1}')
        continua = input('Continuar? [s/n]').upper()
    elif r < 0:
        d = 'descrescente'
        print(f'A razão entre esses números é: {r}, portanto esta progressão aritmética é {d}.')

        termo = int(input('Escolha o termo que você quer saber o valor: '))
        result = n1 + ((termo - 1) * r)

        print(f'O termo {termo} na sua sequência é: \n ...')
        time.sleep(1)
        print(result)
        continua = input('Continuar? [s/n]').upper()
    else:
        d = 'crescente'

        print(f'A razão entre esses números é: {r}, portanto esta progressão aritmética é {d}.')

        termo = int(input('Escolha o termo que você quer saber o valor: '))
        result = n1 + ((termo - 1) * r)

        print(f'O termo {termo} na sua sequência é: \n ...')
        time.sleep(1)
        print(result)
        continua = input('Continuar? [s/n]').upper()
print('/' * 12, ' F I N I S H ', '/' * 12)