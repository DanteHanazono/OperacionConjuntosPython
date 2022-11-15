def llenado(i, u):
    elemento, encontrado = 0, 0
    while encontrado == 0:
        print(f"Digite elemento {i+1}")
        elemento = input()
        for j in range(15):
            if elemento in u:
                encontrado = 1
                break
    return elemento
