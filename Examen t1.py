import random
lista = []

def crearEntrenador(lista):
    entrenador = imput("Ingrese el nombre del entrenador: ")
    pokemon = imput("Ingrese el nombre del pokemon: ")
    ataque =random.randint(150, 250)
    vida = random.randint(500, 900)
    nuevo=(entrenador, pokemon, ataque, vida)
    lista.append(nuevo)
    print("Entrenador agregado exitosamente.")
    
def listaEntrenador(lista):
    for i in range(1, len(lista)):
        for j in range(len(lista)-1):
            if lista[j][2] < lista[j+1][2]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    print("\n==== LISTA DE ENTRENADORES ====\n")
    