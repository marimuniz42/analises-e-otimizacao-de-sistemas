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