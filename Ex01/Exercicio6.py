def main():

    a = int(input('Digite um número: '))
    b = int(input('Digite mais um número: '))
    c = int(input('Digite MAIS UM OUTRO número: '))

    maior = a

    if b > a and b > c:
        maior = b

    if c > a and c > b:
        maior = c

    print(f'O maior número é {maior}')

main()