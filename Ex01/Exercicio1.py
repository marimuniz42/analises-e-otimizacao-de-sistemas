calcular_idade = lambda x: x > 16

ano_atual = int(input('Digite o ano atual: '))
print(f"Você digitou que o ano atual é {ano_atual}")
ano_nascimento = int(input('Digite o ano de nascimento: '))
print(f"Você digitou que o ano de nascimento é {ano_nascimento}")

print("Eleitor" if calcular_idade(ano_atual - ano_nascimento) else "Não pode votar")