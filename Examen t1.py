import random
lista = []
def crearEntrenador(lista):
    entrenador = input("Ingrese el nombre del entrenador: ")
    pokemon = input("Ingrese el nombre del pokemon: ")

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)
    nuevo = (entrenador, pokemon, ataque, vida)

    lista.append(nuevo)

    print("Entrenador agregado exitosamente.")


def listaEntrenador(lista):

    for i in range(1, len(lista)):

        for j in range(len(lista) - 1):

            if lista[j][2] > lista[j + 1][2]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]


    print("\n==== LISTA DE ENTRENADORES ====\n")
    for i in range(len(lista)):
        print(
            i + 1,
            lista[i][0],
            "-",
            lista[i][1],
            "-",
            lista[i][2],
            "-",
            lista[i][3]
        )


def borraPorPokemon(lista):
    if len(lista) == 0:
        print("No hay entrenadores para borrar.")
        return


    vidaBuscar = int(
        input("Ingrese la vida del Pokemon a buscar: ")
    )


    # ORDENAMIENTO POR SELECCION SEGUN LA VIDA

    n = len(lista)
    for manoIzq in range(n):
        ind_min_val = manoIzq

        for vista in range(manoIzq + 1, n):

            if lista[vista][3] < lista[ind_min_val][3]:

                ind_min_val = vista


        lista[manoIzq], lista[ind_min_val] = \
            lista[ind_min_val], lista[manoIzq]


    # BUSQUEDA BINARIA
    menor = 0
    mayor = len(lista) - 1
    posicion = -1

    for data in range(len(lista)):
        medio = (menor + mayor) // 2
        if lista[medio][3] == vidaBuscar:
            posicion = medio
            break

        elif lista[medio][3] < vidaBuscar:
            menor = medio
        else:
            mayor = medio
        if mayor - menor <= 1:
            break

    if posicion == -1:
        if lista[menor][3] == vidaBuscar:

            posicion = menor

        elif lista[mayor][3] == vidaBuscar:

            posicion = mayor
    if posicion != -1:
        print(
            "Pokemon eliminado:",
            lista[posicion][1],
            "- Entrenador:",
            lista[posicion][0]
        )

        lista.pop(posicion)

    else:

        print("No existe un Pokemon con esa vida.")

def peleaPokemon(lista):

    if len(lista) < 2:
        print("Debe haber al menos 2 Pokemon para pelear.")
        return

    listaEntrenador(lista)

    pokemon1 = int(
        input("Seleccione el primer Pokemon: ")
    )

    pokemon2 = int(
        input("Seleccione el segundo Pokemon: ")
    )

    if pokemon1 < 1 or pokemon1 > len(lista):
        print("Primer Pokemon no valido.")
        return


    if pokemon2 < 1 or pokemon2 > len(lista):
        print("Segundo Pokemon no valido.")
        return


    if pokemon1 == pokemon2:
        print("Debe seleccionar dos Pokemon diferentes.")
        return

    pos1 = pokemon1 - 1
    pos2 = pokemon2 - 1

    dato1 = lista[pos1]
    dato2 = lista[pos2]

    numero1 = random.randint(0, 5)
    numero2 = random.randint(0, 5)

    ataque1 = dato1[2] * numero1
    ataque2 = dato2[2] * numero2

    vida1 = dato1[3] - ataque2
    vida2 = dato2[3] - ataque1

    print("\n==== PELEA POKEMON ====\n")

    print(
        dato1[1],
        "ataca con:",
        ataque1
    )

    print(
        dato2[1],
        "ataca con:",
        ataque2
    )

    print(
        dato1[1],
        "queda con vida:",
        vida1
    )

    print(
        dato2[1],
        "queda con vida:",
        vida2
    )

    if vida1 <= 0 and vida2 <= 0:

        print("Ambos Pokemon perdieron.")

        mayor = max(pos1, pos2)
        menor = min(pos1, pos2)

        lista.pop(mayor)
        lista.pop(menor)

    elif vida1 == vida2:

        print("Empate. Ambos Pokemon perdieron.")

        mayor = max(pos1, pos2)
        menor = min(pos1, pos2)

        lista.pop(mayor)
        lista.pop(menor)

    elif vida1 > vida2:

        print(
            "Ganador:",
            dato1[0],
            "-",
            dato1[1]
        )

        lista.pop(pos2)

    else:

        print(
            "Ganador:",
            dato2[0],
            "-",
            dato2[1]
        )

        lista.pop(pos1)

opcion = ""

while opcion != "5":

    print("\n==== Menu ====\n")

    print("1. Crear entrenador")
    print("2. Listar entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelear Pokemon")
    print("5. Finalizar")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            crearEntrenador(lista)

        case "2":
            listaEntrenador(lista)

        case "3":
            borraPorPokemon(lista)

        case "4":
            peleaPokemon(lista)

        case "5":
            print("Finalizando el programa...")

        case _:
            print("Opción inválida.")