import re

palavra = input("Digite uma palavra de entrada: ")

outras_palavras = [ i for i in input("Digite outras palavras separadas por espaço: ").split()] 

esta_no_texto = lambda expressao: re.search(f"^{palavra}",expressao)

array = filter(esta_no_texto,outras_palavras)

array_len = list(array)

print("Tem na lista de palavras" if len(array_len) > 0 else "Não tem na lista de palavras")