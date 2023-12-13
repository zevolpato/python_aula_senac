"""
  Cap05 - Atividade Extra
  Jogo: Papel, pedra e Tesoura

  Objetivos:
  Nesta atividade você vai criar um jogo usando tupla e tupla multi-dimensional.

  Comandos utilizados:
  Tupla, Tupla Multi-Dimensional, biblioteca random e randint
"""
from os import system, name
# biblioteca random
import random

opcao = 's'
contadorJogadas = 0
contadorJogador = 0
contadorComputador = 0
while opcao.upper()=='S':
    system('cls') if(name == 'nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opcao para se jogar: 
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))
    contadorJogadas+=1
    pecas = ("Pedra", "Papel", "Tesoura")
    # lista multi-dimensional
    # nesta lista quando o resultado for -1 o computador ganha, 1 o jogado ganha e 0 deu empate

    if (jogador > 3):
        resultado = 'Você não escolheu um item correto!!!'
    else:
        print('Você escolheu {}' . format(pecas[jogador]))
        print('O computador escolheu: {}' . format(pecas[computador]))
        tabela = ((0, 1, -1),(-1, 0, 1),(1, -1, 0))
        jogada = tabela[computador][jogador]
        if jogada == 0:
            resultado = "Deu empate vocês escolheram a mesma peça"
        elif jogada == 1:
            resultado = "Você ganhou!"
            contadorJogador +=1
        else:
            resultado = "O computador ganhou"
            contadorComputador +=1

    print(resultado)
    opcao=input('Jogar novamente? Aperte S para jogar novamente. ')
    system('cls') if(name == 'nt') else system('clear')
    print('Resultado do Jogo')
    print('Quantidade de jogadas: ', contadorJogadas)
    print(f'Você ganhou {contadorJogador} jogadas ')
    print(f'Você perder {contadorComputador} jogadas ')