import random
import os

#funcion para las opciones
def elegirOpcion():
  #Cual es la responsabilidad de la funcion?
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra,papel o tijera: ')
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opcion no es valida')
    #si no eligio una opcion
    return None, None

  computer_option = random.choice(options)
  print('.' * 15)
  print('User opcion =>', user_option)
  print('Computer opcion =>', computer_option)
  print('.' * 15)
  return user_option, computer_option


def reglasJuego(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_option, computer_option, user_wins, computer_wins


def chekearGanador(user_wins, computer_wins):
  if computer_wins == 2:
    print('El ganador es la computadora')
    return False

  if user_wins == 2:
    print('El ganador es el usuario')
    return False
  return True


def correrJuego():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  bucle = True

  while bucle:

    print('*' * 30)
    print('    ROUND ', rounds)
    print('*' * 30)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = elegirOpcion()

    user_option, computer_option, user_wins, computer_wins = reglasJuego(
      user_option, computer_option, user_wins, computer_wins)
    bucle = chekearGanador(user_wins, computer_wins)

def finalizar():
  fin = input("Desea volver a Jugar?\nEscriba [si] para volver a jugar: ").lower()
  if fin == "si":
    return False
  return True

os.system('clear')
print(" MIGUEL PRODUCTION PRESENT...")
while True:
  correrJuego()
  if finalizar() == True:
    break
print(" END OF THE GAME...")