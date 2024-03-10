SalMin = float(input("Digite o valor do salário mínimo: R$ "))
print("\n")
Nome = input("Digite o seu nome completo: ")
print("\n")
SalBru = float(input("Digite o seu salário bruto: R$ "))

if SalBru<SalMin:
    desc = 2.
    desconto = 2.00
elif SalBru==SalMin:
    desconto = (SalBru*5)/100
    desc = "5%"
else:
    desconto = (SalBru*8)/100
    desc = "8%"

SalFinal = SalBru - desconto

print("\n")

if desc == 2.00:
    print("Caro(a) " + Nome +  ", \n Informamos que o desconto do seu salario foi de R$" + str(desc) + ".\n Tornando assim seu salario liquido igual a " + str(SalFinal) + ";")
else:
    print("Caro(a) " + Nome +  ", \n Informamos que o desconto do seu salario foi de " + str(desc) + ".\n Tornando assim seu salario liquido igual a " + str(SalFinal) + ";")