class Funcionario:
    def __init__(self,nome:str,sexo:str,salario:float):
        e_homem = lambda x: x == 'M'
        descontar_sete_porcento = lambda x: x - (x * 0.07)
        descontar_cinco_porcento = lambda x: x - (x * 0.05)
        self.nome = nome
        salario = descontar_sete_porcento(salario) if e_homem(sexo) else descontar_cinco_porcento(salario)
        self.salario = salario


funcionario = Funcionario(input("Digite o seu nome: "),input("Digite o seu sexo M ou F: "),int(input("Digite o seu salario: ")))

print(f"O funcionario {funcionario.nome} tem um salario de {funcionario.salario}")