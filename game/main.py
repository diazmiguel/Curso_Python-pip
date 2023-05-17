#JUEGO DE PIEDRA PAPEL O TIJERA
import random
import os

print("BIENVENIDO JUGADOR :D")
opciones = ("piedra", "papel", "tijera")
ComputerWin = 0
UserWin = 0
rounds = 1
while True:
  #os.system('clear')
  print("*" * 12 + f"\n ROUND {rounds}\n" + "*" * 12)
  print(f"Computadora: {ComputerWin} | Usuario: {UserWin}")

  opcion = input("¿Piedra, papel o tijera? => ")
  opcion = opcion.lower()

  rounds += 1
  if not opcion in opciones:
    print("Escoge una de las opciones")
  else:
    #Escojemos de forma aleatoria
    ComputerOpcion = random.choice(opciones)
    print(f"Computadora escoje {ComputerOpcion} entonces...")

    if opcion == ComputerOpcion:
      print("EMPATE")
    elif opcion == "piedra":
      if ComputerOpcion == 'tijera':
        print("Piedra gana tijera")
        print("Ganaste!")
        UserWin += 1
      else:  #compOpcion = papel
        print("Papel gana a piedra")
        print("Computer gano!")
        ComputerWin += 1
    elif opcion == 'papel':
      if ComputerOpcion == 'tijera':
        print("Tijera gana a papel")
        print("Computer gano!")
        ComputerWin += 1
      else:  #Computadora = piedra
        print("Papel gana a piedra")
        print("Ganaste!")
        UserWin += 1
    elif opcion == 'tijera':
      if ComputerOpcion == 'papel':
        print("Tijera gana a papel")
        print("Ganaste!")
        UserWin += 1
      else:  #Computadora = piedra
        print("Piedra gana tijera")
        print("Computer gano!")
        ComputerWin += 1
    if ComputerWin == 2:
      print("EL GANADOR ES LA COMPUTADORA")
      break
    if UserWin == 2:
      print("EL GANADOR ES EL USUARIO")
      break
