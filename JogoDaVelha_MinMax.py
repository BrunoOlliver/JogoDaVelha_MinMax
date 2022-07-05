def mostrarGrade(grade):
    print ('-+-+-')
    print (grade[1] + '|' + grade[2] + '|' + grade[3])
    print ('-+-+-')
    print (grade[4] + '|' + grade[5] + '|' + grade[6])
    print ('-+-+-')
    print (grade[7] + '|' + grade[8] + '|' + grade[9])
    print ('-+-+-\n')

def espacoLivre(posicao):
    if (grade[posicao] == ' '):
        return True
    else:
        return False

def inserirSimbolo(simbolo,posicao):
    if espacoLivre(posicao):
        grade[posicao] = simbolo
        mostrarGrade(grade)

        if (verificarEmpate()):
            print("Empate!")
            exit()
        if verificarVitoria():
            if simbolo == 'X':
                print("Maquina Venceu!")
                exit()
            else:
                print("Jogador Venceu!")
                exit()
        return
    else:
        print("Não foi possível inserir aqui!")
        posicao = int(input("Digite a nova posição: "))
        inserirSimbolo(simbolo,posicao)
        return

def verificarVitoria():
    if (grade[1] == grade[2] and grade[1] == grade[3] and grade[1] != ' '):
        return True
    elif (grade[4] == grade[5] and grade[4] == grade[6] and grade[4] != ' '):
        return True
    elif (grade[7] == grade[8] and grade[7] == grade[9] and grade[7] != ' '):
        return True
    elif (grade[1] == grade[4] and grade[1] == grade[7] and grade[1] != ' '):
        return True
    elif (grade[2] == grade[5] and grade[2] == grade[8] and grade[2] != ' '):
        return True
    elif (grade[3] == grade[6] and grade[3] == grade[9] and grade[3] != ' '):
        return True
    elif (grade[1] == grade[5] and grade[1] == grade[9] and grade[1] != ' '):
        return True
    elif (grade[7] == grade[5] and grade[7] == grade[3] and grade[7] != ' '):
        return True
    else:
        return False

def verificarVencedor(escolha):
    if (grade[1] == grade[2] and grade[1] == grade[3] and grade[1] != escolha):
        return True
    elif (grade[4] == grade[5] and grade[4] == grade[6] and grade[4] != escolha):
        return True
    elif (grade[7] == grade[8] and grade[7] == grade[9] and grade[7] != escolha):
        return True
    elif (grade[1] == grade[4] and grade[1] == grade[7] and grade[1] != escolha):
        return True
    elif (grade[2] == grade[5] and grade[2] == grade[8] and grade[2] != escolha):
        return True
    elif (grade[3] == grade[6] and grade[3] == grade[9] and grade[3] != escolha):
        return True
    elif (grade[1] == grade[5] and grade[1] == grade[9] and grade[1] != escolha):
        return True
    elif (grade[7] == grade[5] and grade[7] == grade[3] and grade[7] != escolha):
        return True
    else:
        return False

def verificarEmpate():
    for chave in grade.keys():
        if grade[chave] == ' ':
            return False
    return True


def jogadorMovimento():
    posicao = int(input("Digite a posição para 'O': "))
    inserirSimbolo(jogador,posicao)
    return

def Movimento():
    melhorPontuacao = -800
    melhorMovimento = 0

    for chave in grade.keys():
        if (grade[chave] == ' '):
            grade[chave] = maquina
            pontuacao = minimax(grade,0,False)
            grade[chave] = ' '
            if (pontuacao > melhorPontuacao):
                melhorPontuacao = pontuacao
                melhorMovimento = chave
    inserirSimbolo(maquina,melhorMovimento)
    return

def minimax(grade, profundidade, maximizado):
    if (verificarVencedor(maquina)):
        return 1
    elif (verificarVencedor(jogador)):
        return -1
    elif (verificarEmpate()):
        return 0

    if (maximizado):
        melhorPontuacao = -800
        for chave in grade.keys():
            if (grade[chave] == ' '):
                grade[chave] = maquina
                pontuacao = minimax(grade,profundidade + 1,False)
                grade[chave] = ' '
                if (pontuacao > melhorPontuacao):
                    melhorPontuacao = pontuacao

        return melhorPontuacao

    else:
        melhorPontuacao = 800

        for chave in grade.keys():
            if (grade[chave] == ' '):
                grade[chave] = jogador
                pontuacao = minimax(grade,profundidade + 1, True)
                grade[chave] = ' '
                if (pontuacao < melhorPontuacao):
                    melhorPontuacao = pontuacao
        return melhorPontuacao

grade = {1: ' ',2: ' ', 3: ' ',
         4: ' ',5: ' ', 6: ' ',
         7: ' ',8: ' ', 9: ' '}

print ("#### Jogo da Velha ####")
print ("\n REGRAS DO JOGO:")
print ("1. Uma posição indica onde será sua escolha")
print ("2. O Computador começa primeiro")
print ("3. O seu simbolo é o 'O'\n")
print ("Segue as posições:\n")
print ("| 1 | 2 | 3 |")
print ("| - + - + - |")
print ("| 4 | 5 | 6 |")
print ("| - + - + - |")
print ("| 7 | 8 | 9 |\n")

jogador = 'O'
maquina = 'X'

global firstComputerMove
firstComputerMove = True

while not verificarVitoria():
    Movimento()
    jogadorMovimento()
