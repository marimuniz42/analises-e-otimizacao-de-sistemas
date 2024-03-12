# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if numero1 > numero2:
    print("O primeiro número ({}) é maior que o segundo número ({})".format(numero1, numero2))
else:
    print("O segundo número ({}) é maior que o primeiro número ({})".format(numero2, numero1))