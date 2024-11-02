#Importação de bibliotecas
import time, random

#Declaração dos dicionários
ranking_modo1 = {
    'nome': [],
    'pontos': []
}
ranking_modo2 = {
    'nome': [],
    'pontos': []
}
ranking_modo3 = {
    'nome': [],
    'pontos': []
}

#Função onde ocorre o modo 1 do quiz
def modo1_quiz():
    pontos = 0

#Função onde ocorre o modo 2 do quiz
def modo2_quiz():
    pontos = 0

#Função onde ocorre o modo 3 do quiz
def modo3_quiz():
    pontos = 0

#Função que mostra o ranking de acrodo com o modo do quiz
def mostra_ranking(modo):
    with open(f'ranking/ranking_modo{modo}.txt', 'r') as ranking:
        for linha in ranking:
            print(linha)
    ranking.close()

#Looping principal do código
while True:
    print('Olá, seja bem-vindo ao AskMe!')
    op = int(input('1. Começar\n2. Hall da Fama\n0. Sair\n'))
    #Condição se a opção for 0
    if op == 0:
        print('Até Mais! Obrigdao por Jogar!')
        break
    #Condição se a opção for 1
    elif op == 1:
        while True:
            print('Modo do Quiz')
            op = int(input('1. Questões Fixas\n2. Limite de Tempo\n3. Tente não Errar\n'))
            if op == 1:
                modo1_quiz()
                break
            elif op == 2:
                modo2_quiz()
                break
            elif op == 3:
                modo3_quiz()
                break
            else:
                print('Opção Inválida! Digite Novamente.')
    #Condição se a opção for 2
    elif op == 2:
        while True:
            print('Hall da Fama')
            modo = int(input('1. Questões Fixas\n2. Limite de Tempo\n3. Tente não Errar\n'))
            #Condição se a opção for 1, 2 ou 3
            if modo == 1 or modo == 2 or modo == 3:
                mostra_ranking(modo)
                break
            #Condição se a opção não for 1, 2 ou 3
            else:
                print('Opção Inválida! Digite Novamente.')
    #Condição se a opção não for 0, 1 ou 2
    else:
        print('Opção Inválida! Digite Novamente.')