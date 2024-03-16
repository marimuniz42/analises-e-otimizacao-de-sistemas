# Enunciado da questão

Crack de Senha: Escreva um programa que tente decifrar uma senha de 4 dígitos numéricos através de busca exaustiva.

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

# Enunciado da questão

Subconjunto com Soma Específica: Dado um conjunto de números inteiros e um valor de soma, crie um algoritmo que encontre todos os subconjuntos possíveis cuja soma seja igual ao valor dado.

```py

```
# Enunciado da questão

Permutações de uma String: Implemente um algoritmo que gere todas as permutações possíveis de uma string dada.

```py

```
# Enunciado da questão

Combinações de Moedas: Dado um conjunto de valores de moedas e um valor total, encontre todas as maneiras possíveis de combinar as moedas para alcançar o valor total.

```py

```
# Enunciado da questão

Problema do Caixeiro Viajante: Implemente uma solução de força bruta para o Problema do Caixeiro Viajante, onde você deve encontrar o caminho mais curto que passa por todas as cidades uma única vez e retorna à cidade de origem.

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
# Enunciado da questão

Máximo Subarray: Crie um algoritmo que encontre o subarray contíguo dentro de um array de números que tem a maior soma.

```py

```
# Enunciado da questão

Anagramas de Palavra: Dada uma palavra, escreva um programa que encontre todos os anagramas possíveis desta palavra.

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
# Enunciado da questão

Horários de Reunião: Dada uma lista de horários disponíveis para um grupo de pessoas, encontre todos os intervalos de tempo possíveis onde todos podem se reunir.

```py

```
# Enunciado da questão

Quebra de Código de Cofre: Suponha que um cofre é aberto com uma sequência específica de N botões pressionados. Desenvolva um algoritmo que tente todas as combinações possíveis até encontrar a sequência correta.

```py

```