# Semana 2

## Crack de Senha:

Escreva um programa que tente decifrar uma senha de 4 dígitos numéricos através de busca exaustiva.

```py
senha = 4321
lista = set()

for i in range(10000):
    lista.add(str(i).zfill(4))

for elemento in lista:
    print(elemento)
    if elemento == str(senha):
        print(elemento)
        break
```

## Subconjunto com Soma Específica:

Dado um conjunto de números inteiros e um valor de soma, crie um algoritmo que encontre todos os subconjuntos possíveis cuja soma seja igual ao valor dado.

```py
def find_subconjunto(nums, resp):
    def backtrack(start, path, curr_sum):
        if curr_sum == resp:
            result.append(path)
            return
        if curr_sum > resp:
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]], curr_sum + nums[i])

    result = []
    backtrack(0, [], 0)
    return result

nums = [33, 20, 15, 33, 40, 51, 46, 26]
resp = 66
subsets = find_subconjunto(nums, resp)
print(f"Subconjuntos cuja soma é {resp}:", (subsets))
```
## Permutações de uma String:

Implemente um algoritmo que gere todas as permutações possíveis de uma string dada.

```py
from itertools import permutations

def gerar_permutacao(string):
    perm = permutations(string)
    
    per_list = [''.join(per) for per in perm]
    
    return per_list

ler_string = "abcd"
resultado = gerar_permutacao(ler_string)
print("Permutações de",ler_string,":",resultado)
```
## Combinações de Moedas: 

Dado um conjunto de valores de moedas e um valor total, encontre todas as maneiras possíveis de combinar as moedas para alcançar o valor total.

```py
def encontrar_combinacoes_moedas(valores_moedas, total):
    def encontrar_combinacoes(total_atual, indice_moeda, combinacao_atual, todas_combinacoes):
        if total_atual == 0:
            todas_combinacoes.append(combinacao_atual)
            return
        
        if total_atual < 0 or indice_moeda >= len(valores_moedas):
            return
        
        encontrar_combinacoes(total_atual - valores_moedas[indice_moeda], indice_moeda, combinacao_atual + [valores_moedas[indice_moeda]], todas_combinacoes)
        encontrar_combinacoes(total_atual, indice_moeda + 1, combinacao_atual, todas_combinacoes)

    todas_combinacoes = []
    encontrar_combinacoes(total, 0, [], todas_combinacoes)

    return todas_combinacoes

valores_moedas = [1, 2, 5]  
total = 5  
combinacoes = encontrar_combinacoes_moedas(valores_moedas, total)
print("Número de combinações possíveis:", len(combinacoes))
print("Combinações:")
for combinacao in combinacoes:
    print(combinacao)
```
## Problema do Caixeiro Viajante: 

Implemente uma solução de força bruta para o Problema do Caixeiro Viajante, onde você deve encontrar o caminho mais curto que passa por todas as cidades uma única vez e retorna à cidade de origem.

```py
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("A", "D", weight=5)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=2)
G.add_edge("C", "D", weight=3)

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


try:
    from networkx.algorithms.approximation import traveling_salesman_problem
    tsp_solution = traveling_salesman_problem(G, cycle=True)
    
    print("Solução do TSP (ordem das cidades):", tsp_solution)
except ImportError as e:
    print("Para resolver o TSP, instale o pacote scipy: pip install scipy")
```
## Máximo Subarray:

Crie um algoritmo que encontre o subarray contíguo dentro de um array de números que tem a maior soma.

```py
def max_nums(array:list) -> list:
    sub_array = list()
    for i in range(4):
        sub_array.append(max(array))
        del array[array.index(sub_array[i])]

    return sub_array

array = [11, -3, 20, -17, 25, 10, 9, -4, 5]
array = max_nums(array)

print(f"O array é {array} e a soma é: {sum(array)}")
```
## Anagramas de Palavra: 

Dada uma palavra, escreva um programa que encontre todos os anagramas possíveis desta palavra.

```py
import itertools

def todos_os_anagramas(palavra:str) -> list:
    anagramas = set(itertools.permutations(palavra))
    anagramas_unicos = [''.join(anagrama) for anagrama in anagramas]
    return anagramas_unicos
        
palavra = input("Digite uma palavra: ")
anagramas_unicos = todos_os_anagramas(palavra)

for i, palavra in enumerate(anagramas_unicos):
    print(f"{i}) {palavra}")
```
## Horários de Reunião: 

Dada uma lista de horários disponíveis para um grupo de pessoas, encontre todos os intervalos de tempo possíveis onde todos podem se reunir.

```py
from typing import List, Tuple

def fundir_intervalos(intervalos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervalos:
        return []

    intervalos.sort(key=lambda x: x[0])
    fundidos = [intervalos[0]]
    
    for inicio, fim in intervalos[1:]:
        if inicio <= fundidos[-1][1]:
            fundidos[-1] = (fundidos[-1][0], max(fundidos[-1][1], fim))
        else:
            fundidos.append((inicio, fim))
    
    return fundidos

def encontrar_intervalos_disponiveis(horarios: List[List[Tuple[int, int]]], duracao_minima: int) -> List[Tuple[int, int]]:
    horarios_concatenados = [slot for agenda_pessoa in horarios for slot in agenda_pessoa]
    horarios_fundidos = fundir_intervalos(horarios_concatenados)
    
    intervalos_disponiveis = []
    for i in range(1, len(horarios_fundidos)):
        inicio = horarios_fundidos[i - 1][1]
        fim = horarios_fundidos[i][0]
        duracao = fim - inicio
        if duracao >= duracao_minima:
            intervalos_disponiveis.append((inicio, fim))
    
    return intervalos_disponiveis

horarios = [
    [(9, 10), (12, 13), (14, 15)],
    [(8, 9), (11, 12), (13, 14)],
    [(10, 11), (12, 13), (15, 16)]
]
duracao_minima = 1
intervalos_disponiveis = encontrar_intervalos_disponiveis(horarios, duracao_minima)
print("Intervalos disponíveis para reunião:")
for inicio, fim in intervalos_disponiveis:
    print(f"Das {inicio} às {fim}")
```
## Quebra de Código de Cofre: 

Suponha que um cofre é aberto com uma sequência específica de N botões pressionados. Desenvolva um algoritmo que tente todas as combinações possíveis até encontrar a sequência correta.

```py
def quebra_senha(sequencia_correta, sequencia_atual, comprimento_sequencia, tentativas):
    if len(sequencia_atual) == comprimento_sequencia:
        if sequencia_atual == sequencia_correta:
            print("Sequência correta encontrada:", sequencia_atual)
            return True
        else:
            return False
    
    for botao in range(1, 10):
        if quebra_senha(sequencia_correta, sequencia_atual + [botao], comprimento_sequencia, tentativas + [sequencia_atual + [botao]]):
            return True
        else:
            print("Tentativa:", sequencia_atual + [botao])

    return False

def iniciar_quebra_senha(sequencia_correta, comprimento_sequencia):

    quebra_senha(sequencia_correta, [], comprimento_sequencia, [])

sequencia_correta = [1, 3, 5, 7, 9]
comprimento_sequencia = len(sequencia_correta)
iniciar_quebra_senha(sequencia_correta, comprimento_sequencia)
```