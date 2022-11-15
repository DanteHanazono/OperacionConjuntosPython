from mostrarConjuntos import mostrar


def diferencia(cadenaVacia, ancho, relleno2, relleno1, mensaje, opcion, cA, cB, A, B, C):
    m = 0
    print(cadenaVacia.center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print(mensaje[opcion].center(ancho, relleno2))
    for i in range(cA):
        for j in range(cB):
            if A[i] == B[j]:
                break
            if j == cB - 1:
                C.insert(m, A[i])
                m += 1
    mostrar(A, cA, "A")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(B, cB, "B")
    print(cadenaVacia.center(ancho, relleno2))
    mostrar(C, m, "A - B")
    print(cadenaVacia.center(ancho, relleno1))
    print(cadenaVacia.center(ancho, relleno2))
