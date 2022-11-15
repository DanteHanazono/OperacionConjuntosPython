from llenar import llenando
from unionConjunto import union
from interseccionConjunto import interseccion
from diferenciaConjunto import diferencia

opcion, cA, cB = 0, 0, 0
u = ("0", "1", "2", "3", "4", "5", "6", "7",
     "8", "9", "0", "a", "e", "i", "o", "u")
A = []
B = []
C = []
ancho = 40
relleno1 = "-"
relleno2 = " "
cadenaVacia = ""
mensaje = ("MENU DE OPCIONES", "LLENADO DE CONJUNTOS", "UNION DE CONJUNTOS",
           "INTERSECCION DE CONJUNTOS", "DIFERENCIA DE CONJUNTOS", "SALIENDO DEL PROGRAMA")

while opcion != 5:
    print(cadenaVacia.center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print(mensaje[opcion].center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print("1. Llenado de conjuntos")
    print("2. Union de conjuntos")
    print("3. Interseccion de conjuntos")
    print("4. Diferencia de conjuntos")
    print("5. SALIR")
    print(cadenaVacia.center(ancho, relleno1))
    print(cadenaVacia.center(ancho, relleno2))

    opcion = int(input())
    if cA == 0 and opcion < 5:
        print(cadenaVacia.center(ancho, relleno2))
        print(cadenaVacia.center(ancho, relleno1))
        print(mensaje[opcion].center(ancho, relleno2))
        print(cadenaVacia.center(ancho, relleno2))
        print("Ingrese el tamaño de los conjuntos A y B")
        cA = int(input("Tamaño del conjunto A: "))
        cB = int(input("Tamaño del conjunto B: "))

    if opcion == 1:
        llenando(cA, A, u, cB, B, cadenaVacia, ancho, relleno2, relleno1)

    elif opcion == 2:
        union(cadenaVacia, ancho, relleno2, relleno1,
              mensaje, opcion, cA, C, A, cB, B)

    elif opcion == 3:
        interseccion(cadenaVacia, ancho, relleno2, relleno1,
                     mensaje, opcion, cA, cB, A, B, C)

    elif opcion == 4:
        diferencia(cadenaVacia, ancho, relleno2, relleno1,
                   mensaje, opcion, cA, cB, A, B, C)

    elif opcion == 5:
        print(cadenaVacia.center(ancho, relleno2))
        print(cadenaVacia.center(ancho, relleno1))
        print(mensaje[opcion].center(ancho, relleno2))
        print(cadenaVacia.center(ancho, relleno1))
        break

    else:
        print(cadenaVacia.center(ancho, relleno2))
        print("Digite una opcion valida")

    opcion = 0
