from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
maquina = randint(0, 2)

player_name = input("Digite seu nome: ")

def fechar():
    if player == 3:
        return
    
print(f'''Olá {player_name}, selecione a opção desejada:
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura
[ 3 ] Fecha o Jogo''')

while True:
    player = int(input("Qual é sua jogada? "))
    if player > 3:
        print("\n JOGO: Escolha um número entre 0 e 3 \n")
    elif player == 3:
        print("Fechando o jogo...")
        break
    elif player <= 3 :
        print("1...")
        sleep(0.5)
        print("2...")
        sleep(0.5)
        print("3...")
        sleep(0.5)
        print("E... Já!")

        print("=" * 23)
        print(f"A Maquina jogou {itens[maquina]}")
        print(f"{player_name} jogou {itens[player]}")
        print("=" * 23)

    if maquina == 0:
        if player == 0:
            print("\nEmpate! >=( \n")
        elif player == 1:
            print("\nJogador Wins, Grrr!\n")
        elif player == 2:
            print("\nMaquina Wins, Easy Game!\n")
        elif player >= 3:
            print("\nMaquina: que cê tá fazendo menó\n")

    elif maquina == 1:
        if player == 0:
            print("\nMaquina Wins, Easy Game!\n")
        elif player == 1:
            print("\nEmpate! >=( \n")
        elif player == 2:
            print("\nJogador Wins, Grrr!\n")
        elif player >= 3:
            print(f"\nMaquina: que cê tá fazendo menó\n")
        

    elif maquina == 2:
        if player == 0:
            print("\nJogador Wins, Grrr!\n")
        elif player == 1:
            print("\nMaquina Wins, Easy Game!\n")
        elif player == 2:
            print("\nEmpate! >=( \n")
        elif player >= 3:
            print("\nMaquina: que cê tá fazendo menó\n")
        