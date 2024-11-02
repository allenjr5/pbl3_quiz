with open('teste/teste.txt', 'r') as teste:
    for linha in teste:
        texto = linha
        print(texto, end='')
    print()
teste.close()