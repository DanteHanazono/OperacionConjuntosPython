from llenadoConjunto import llenado


def llenando(cA, A, u, cB, B, cadenaVacia, ancho, relleno2, relleno1):
    i = 0
    print(" ")
    print("Elementos del conjunto A")
    while i != cA:
        A.insert(i, llenado(i, u))
        if i > 0:
            for j in range(i):
                if A[j] == A[i]:
                    print("Este valor ya esta registrado")
                    i = i-1
                    break
        i += 1

    i = 0
    print(" ")
    print("Elementos del conjunto B")
    while i != cB:
        B.insert(i, llenado(i, u))
        if i > 0:
            for j in range(i):
                if B[j] == B[i]:
                    print("Este valor ya esta registrado")
                    i = i-1
                    break
        i += 1

    print(cadenaVacia.center(ancho, relleno2))
    print(cadenaVacia.center(ancho, relleno1))
    print("Conjunto A:{", end='')
    for i in range(cA):
        if i < cA-1:
            print(f"{A[i]},", end=' ')
        else:
            print(A[i], end='')
    print("}")
    print("Conjunto B:{", end='')
    for i in range(cB):
        if i < cB-1:
            print(f"{B[i]},", end=' ')
        else:
            print(B[i], end='')
    print("}")
    print(cadenaVacia.center(ancho, relleno1))
    print(cadenaVacia.center(ancho, relleno2))
