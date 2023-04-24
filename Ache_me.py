from random import shuffle#Para embaralhar o arrey
from random import choice#Escolher um elemento "aleatorio"

def menu():
    print("------------------------------------------------------------------------------------------\n")
    print('        Bem vindo!        ')
    print("\n      ---------------\n      | |1-Iniciar| |    \n      ---------------\n      | |2-Regras | |    \n      ---------------\n      | | 3-Sair  | |    \n      ---------------")
 
    try:
        entrar = int(input('\nEscolha aqui a opção: '))
        print("")
        
        if entrar == 1:
            jogo()#Iniciar o programa
            continuar()#Vai para a função perguntando se quer continuar ou não
        
        elif entrar == 2:
            regras()

        elif entrar == 3:
            sair()

        else:
            print('Escolha 1, 2 ou 3')
            menu()
    except ValueError:
        print('Escolha 1, 2 ou 3')
        menu()
#------------------------------------------------------------------------------------------------------------------------
def regras():
    print("------------------------------------------------------------------------------------------\n")
    print('Então você chegou agora né?!')
    print('Vamos explicar')
    print('1-Será dado um baralho de poker de A a K')
    print('2-Esse baralho será embaralhado ')
    print('3-Uma carta será escolhida e você tem que achar ela na sorte em um número determinado de turnos')
    print('4-Você botará um posição de 0 a 12 para escolher um carta')
    print("5-Se tiver sorte a carta escolhida será a que você precisava achar")
    print('6-Se tiver azar o jogo continuará até ou os turnos acabarem ou você achar a carta premiada')
    print("")
    print('Espero ter ajuda e bom jogo\n')
    print('              --------')
    print('             |4-Voltar|')
    print('              --------')

    try:
        voltar = int(input('Escreva aqui: '))
        print('\n')
        if voltar == 4:
            menu()
        else:
            print('Aperte 4 para sair!')
            regras()
    except ValueError:
        print('Aperte 4 para sair!')
        regras()

#------------------------------------------------------------------------------------------------------------------------
def sair():
    print('Tem certeza?')
    print(' ------     ------')
    print('|1-SIM |   |2-NÂO |')
    print(' ------     ------')

    try:
        quer = int(input())
        if quer == 1:
            print('Até a próxima!')
        elif quer == 2:
            menu()
        else:
            print('Tem que ser 1 ou 2')
            sair()

    except ValueError:
        print('Tem que ser 1 ou 2')
        sair()
#---------------------
def continuar():
    print('Quer reiniciar?')
    print(' ------     ------')
    print('|1-SIM |   |2-NÂO |')
    print(' ------     ------')

    try:
        quer = int(input())
        if quer == 1:
            jogo()
            continuar()
        elif quer == 2:
            print('Até a próxima!')

        else:
            print('Tem que ser 1 ou 2')
            continuar()

    except ValueError:
        print('Tem que ser 1 ou 2')
        continuar()
#-----------------------------------------------------------------------------------------------------------------------
def carta(cartas):
    if cartas  == 'A':
        print(' ____')
        print('|°   |')
        print('| A  |')
        print('|___°|')

    elif cartas  == '2':
        print(' ____')
        print('|°   |')
        print('| 2  |')
        print('|___°|')

    elif cartas  == '3':
        print(' ____')
        print('|°   |')
        print('| 3  |')
        print('|___°|')

    elif cartas  == '4':
        print(' ____')
        print('|°   |')
        print('| 4  |')
        print('|___°|')

    elif cartas  == '5':
        print(' ____')
        print('|°   |')
        print('| 5  |')
        print('|___°|')

    elif cartas  == '6':
        print(' ____')
        print('|°   |')
        print('| 6  |')
        print('|___°|')

    elif cartas  == '7':
        print(' ____')
        print('|°   |')
        print('| 7  |')
        print('|___°|')

    elif cartas  == '8':
        print(' ____')
        print('|°   |')
        print('| 8  |')
        print('|___°|')

    elif cartas  == '9':
        print(' ____')
        print('|°   |')
        print('| 9  |')
        print('|___°|')

    elif cartas  == '10':
        print(' ____')
        print('|°   |')
        print('| 10 |')
        print('|___°|')

    elif cartas  == 'J':
        print(' ____')
        print('|°   |')
        print('| J  |')
        print('|___°|')

    elif cartas  == 'Q':
        print(' ____')
        print('|°   |')
        print('| Q  |')
        print('|___°|') 

    elif cartas  == 'K':
        print(' ____')
        print('|°   |')
        print('| K  |')
        print('|___°|')
#-----------------------------------------------------------------------------------------------------------------
def jogo():
    #Variaveis
    print("------------------------------------------------------------------------------------------\n")
    cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    escolhida = choice(cartas)#Escolher uma carta
    tempo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    contador = choice(tempo)#Escolher um tempo
    nao = [
        'Não foi dessa vez', 'Puts...', 'Que maré de Azar', 
        'Não é possivel', 'Na próxima vai, confia',
        'Que pena', 'Foi um balde de água fria nos seus planos'
        ]

    #Imprimir os textos
    print(f'{cartas}\n')
    print(f'Tente achar o {escolhida} em {contador} turnos\n')#A carta desejada e o numero de turnos
    print('Embaralhando...')
    shuffle(cartas)#Embaralhar o deck

    turno = 1 #Em qual turno est[a]
    print(f'Turno {turno}')

    try:#Isso vai acontecer se o jogador botar a posição que ta no arrey
        cont = int(input('Escolha uma posição: '))#A posição escolhida pelo jogador

        while contador > 0:#Enquanto não chegar a 0
            turno += 1#Vai aumentar ao longo do jogo
            contador -= 1#Vai diminuir ao longo do jogo
            print(f'\nSua carta é:')#A carta da posição escolhida
            carta(cartas[cont])#Vai para função que imprime a carta que foi escolhida
            #print(f'\n{cartas}\n')#Como ficou o deck desse turno

            if cartas[cont] == escolhida: #Se a carta escolhida bater com a carta desejada
                print('Parabens você ganhou!')
                contador = 0#Para sair do while automaticamente

            else:
                if contador != 0: #Se nãofor 0 o contador
                    print(f'{choice(nao)}\n')

                    #shuffle(cartas) #Embaralha novamente
                    #print('Embaralhando...')
                    print(f'Turno {turno}')
                    cont = int(input('Escolha uma posição: '))#Outra tentativa

                else: #Quando chega em 0
                    print('Você perdeu')

        print('O jogo acabou') #Quando sai do While

#-------------------------------------------------------------------------------------------------------------------
    except IndexError: #Casa a posição que o jogador botou não esteja no arrey 

        print("\ntem que ser em 0 a 12")
        print('Tente novamente\n')
        jogo()#Vai reiniciar o jogo todo

    except ValueError: #Casa a posição que o jogador botou não esteja no arrey 
        print("-----------------------")
        print("|tem que ser em 0 a 12 |")
        print('|  Tente novamente     |')
        print("-----------------------")
        jogo()#Vai reiniciar o jogo todo

menu()
