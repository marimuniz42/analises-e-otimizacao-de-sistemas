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