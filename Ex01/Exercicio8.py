a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a != b and a != c and b != c:
    print(f"Números em ordem decrescente: {max(a, b, c)}, {sorted([a, b, c], reverse=True)[1]}, {min(a, b, c)}")

    for num in [a, b, c]:
        paridade = "par" if num % 2 == 0 else "ímpar"
        print(f"O número {num} é {paridade}.")

else:
    print("Por favor, digite três números inteiros diferentes.")