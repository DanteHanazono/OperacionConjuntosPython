from mostrarConjuntos import mostrar


def union(cadenaVacia, ancho, relleno2, relleno1, mensaje, opcion, cA, C, A, cB, B):
    k = 0
    print(cadenaVacia.center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print(mensaje[opcion].center(ancho, relleno2))
    for i in range(cA):
        C.insert(k, A[i])
        k += 1
    for i in range(cB):
        encontrado = 0
        for j in range(cA):
            if A[j] == B[i]:
                encontrado = 1
                break
        if encontrado == 0:
            C.insert(k, B[i])
            k += 1
    mostrar(A, cA, "A")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(B, cB, "B")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(C, k, "A U B")
    print(cadenaVacia.center(ancho, relleno1))
    print(cadenaVacia.center(ancho, relleno2))
