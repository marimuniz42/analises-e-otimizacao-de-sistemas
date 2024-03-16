senha = 4321
lista = set()

for i in range(10000):
    lista.add(str(i).zfill(4))

for elemento in lista:
    print(elemento)
    if elemento == str(senha):
        print(elemento)
        break