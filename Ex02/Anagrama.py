import itertools

def todos_os_anagramas(palavra:str) -> list:
    anagramas = set(itertools.permutations(palavra))
    anagramas_unicos = [''.join(anagrama) for anagrama in anagramas]
    return anagramas_unicos
        
palavra = input("Digite uma palavra: ")
anagramas_unicos = todos_os_anagramas(palavra)

for i, palavra in enumerate(anagramas_unicos):
    print(f"{i}) {palavra}")