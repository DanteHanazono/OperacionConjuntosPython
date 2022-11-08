from mostrarConjuntos import mostrar


def interseccion(cadenaVacia, ancho, relleno2, relleno1, Mensaje, opcion, cA, cB, A, B, C):
    l = 0
    print(cadenaVacia.center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print(Mensaje[opcion].center(ancho, relleno2))
    for i in range(cA):
        for j in range(cB):
            if A[i] == B[j]:
                C.insert(l, A[i])
                l += 1
    mostrar(A, cA, "A")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(B, cB, "B")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(C, l, "A n B")
    print(cadenaVacia.center(ancho, relleno1))
    print(cadenaVacia.center(ancho, relleno2))
