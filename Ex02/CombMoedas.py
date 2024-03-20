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