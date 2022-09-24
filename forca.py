import os
import random

nome = input("Digite seu nome:")
print(f'Seeja bem vindo ao jogo {nome}! Vamos começar?')
input('\nPressione enter para começar')
os.system('cls')

lista_de_palavras_secretas = ['panqueca', 'chocolate', 'brigadeiro','cachorro']
palavra_selecionada = random.choice(lista_de_palavras_secretas).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_'] * tamanho_palavra
qtd_erros = 0

while '_' in palavra_codificada and qtd_erros < 3:
    print(f'\nSua palavra tem {tamanho_palavra} letras, o tema é comida ou um animal. O jogo que decide')
    print(f'Erro: {qtd_erros} de 3')
    for letra in palavra_codificada:
        print(letra,end=' ')
        print()

        letra_escolhida = input('Digite uma letra: ').upper()
        acertou = False
        for i in range(len(palavra_selecionada)):
            if letra_escolhida == palavra_selecionada[i]:
                palavra_codificada [i] = letra_escolhida
                acertou = True

        if acertou == True:
            print('Parabéns aceertou miserave.')
        else:
            print('EROOOOU!! Essa letra não existe no jogo')
            qtd_erros = qtd_erros + 1

    if qtd_erros ==3:
        print('Não acredito que vai dar forca, tristeza total')
    else:
        print('\nUFAAA! Parabéns você é um vencedor\n')

    print(f'A palavra era: {palavra_selecionada}')