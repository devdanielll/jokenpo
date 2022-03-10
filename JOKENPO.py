from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
maquina = randint(0, 2)
print('''Opções:
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura''')

player = int(input("Qual é sua jogada? "))
print("1...")
sleep(0.5)
print("2...")
sleep(0.5)
print("3...")
sleep(0.5)
print("E... Já!")

print("=" * 15)
print(f"A Maquina jogou {itens[maquina]}")
print(f"O Player jogou {itens[player]}")
print("=" * 15)

if maquina == 0:
  if player == 0:
    print("Empate! >=( ")
  elif player == 1:
    print("Jogador Wins, Grrr!")
  elif player == 2:
    print("Maquina Wins, Easy Game!")
  else:
    print("ERRO!")

elif maquina == 1:
  if player == 0:
    print("Maquina Wins, Easy Game!")
  elif player == 1:
    print("Empate! >=( ")
  elif player == 2:
    print("Jogador Wins, Grrr!")
  else:
    print("ERRO!")

elif maquina == 2:
  if player == 0:
    print("Jogador Wins, Grrr!")
  elif player == 1:
    print("Maquina Wins, Easy Game!")
  elif player == 2:
    print("Empate! >=( ")
  else:
    print("ERRO!")