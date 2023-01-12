from random import choice
from time import sleep
list = []
valor = ''
acabar = 0
escolha = 0
quantia = 0
termo = 0
print('Bem-vindo ao programa de escolha interativo de randomização!''')
while escolha != 3:
    escolha = int(input('''Escolha no menu interativo qual a opção que mais se adequa:
    \033[1;32m[ 1 ] - Eu quero randomizar um número específico de palavras.
    \033[1;32m[ 2 ] - Eu não sei quantas palavras serão.
    \033[1;31m[ 3 ] - Quero encerrar o programa! 
    '''))
    if escolha == 1:
        quantia = int(input('Informe a quantia de palavras: '))
        for c in range(0, quantia+1):
            valor = input('Digite um termo: ').upper()
            list.append(valor)
            termo += 1
            if termo == quantia:
                resultado = choice(list)
                print('A palavra escolhida foi: ', resultado, '\n')
                sleep(5)
                list.clear()
                break
    elif escolha == 2:
        print('-=' * 15)
        print('Para parar, escreva: PARAR')
        print('-=' * 15)
        while valor != 'parar':
            valor = input('Digite um termo: ').upper()
            list.append(valor)
            if valor == 'PARAR':
                list.pop()
                break
        resultado = choice(list)
        print('A palavra escolhida foi: ', resultado, '\n')
        sleep(5)
        list.clear()
    elif escolha == 3:
        break
    if escolha >= 4:
        print('VALOR INVÁLIDO. TENTE NOVAMENTE!')

