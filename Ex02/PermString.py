from itertools import permutations

def gerar_permutacao(string):
    perm = permutations(string)
    
    per_list = [''.join(per) for per in perm]
    
    return per_list

ler_string = "abcd"
resultado = gerar_permutacao(ler_string)
print("Permutações de",ler_string,":",resultado)