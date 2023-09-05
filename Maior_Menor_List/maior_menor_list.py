import time

print('-' * 12, ' ANÁLISE DE UMA LISTA DE VALORES ', '-' * 12)

lista = []
e = int(input('Quantos valores vocẽ quer inserir na lista? '))
print(f'Ok. Insira os {e} valores abaixo e te mostrarei: o maior ou menor da sequênciaa, e a soma da lista!')
for c in range(0, e):
    value = int(input('Insira o valor: '))
    lista.append(value)
print(f'Esta é a lista: {lista}')
continua = 'S'
while continua == 'S':
    option = input('Digite o que deseja:\n Maior [maior]\n Menor [menor]\n Soma [soma]').upper()
    match option:
        case 'MAIOR':
            maior = max(lista)
            print(f'O maior valor da lista é: {maior}')
            continua = input('Quer repetir? [s/n]').upper()
        case 'MENOR':
            menor = min(lista)
            print(f'O menor valor da lista é: {menor}')
            continua = input('Quer repetir? [s/n]').upper()
        case 'SOMA':
            soma_ = sum(lista)
            print(f'A soma dos valores da lista é: {soma_}')
            continua = input('Quer repetir? [s/n]').upper()
print('-' * 12, ' F I N I S H ', '-' * 12)
