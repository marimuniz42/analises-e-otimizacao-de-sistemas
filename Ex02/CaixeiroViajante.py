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