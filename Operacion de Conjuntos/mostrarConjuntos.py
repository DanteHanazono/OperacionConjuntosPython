def mostrar(a, b, l):
    print(f"{l}=", end='')
    print("{", end='')
    for i in range(b):
        if i == 0:
            print(a[i], end='')
        else:
            print(f", {a[i]}", end='')
    print("}")
