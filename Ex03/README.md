# Semana 3

## Exercício 1:

 Implemente o algoritmo de busca de palavras em texto usando a abordagem de força bruta em Python. Teste o algoritmo buscando a palavra "exemplo" em um texto de sua escolha.

```py
texto = """
sufflate degenerated chrism reformism unclearest coonties pessary hepatopancreas
es vitrifactures terakihi paralinguistic hagdowns unsifted buzzards worthlessly 
bourgeoises induplicated epidemicity daughters sharesmen upstandingness matellas
se landslide drowning anteceded forslacking foresails obsessor bravely keavie mo
nishes querier marlingspike noticeable temporisings paramnesia freezingly coadmi
tting koodoo subprograms ginzo dolomitization scrawninesses sheath computerized 
empeaching reciprocant discord sawyer chloritisations untractableness untiring e
xemplo backfires incrusts regenerates haywire intricately monachal atheneum maw 
wallyballs troilites batmitzvahs projectures rhizocarpic strimming disload parvo
virus sundras hyponastically disclamations enlivening copping uprated planimetri
cal fiancee underlayments replaced humbugger counterbracing hypophysectomy overb
leached pleurae pinkoes hairifs disappearance jarks defrauder northward captives
 basement getting gallized theriomorphisms psychophysics attuiting totanus unpot
ted revegetates antimutagens sitter
"""

print("Está no texto" if texto.find("exemplo") else "Não está")
```

## Exercício 2:

Modifique o algoritmo de força bruta para registrar o número total de comparações de caracteres realizadas durante a busca. Analise a eficiência do algoritmo com base nesse número.

```py
import time 

inicio = time.time()

texto = """
sufflate degenerated chrism reformism unclearest coonties pessary hepatopancreas
es vitrifactures terakihi paralinguistic hagdowns unsifted buzzards worthlessly 
bourgeoises induplicated epidemicity daughters sharesmen upstandingness matellas
se landslide drowning anteceded forslacking foresails obsessor bravely keavie mo
nishes querier marlingspike noticeable temporisings paramnesia freezingly coadmi
tting koodoo subprograms ginzo dolomitization scrawninesses sheath computerized 
empeaching reciprocant discord sawyer chloritisations untractableness untiring e
xemplo backfires incrusts regenerates haywire intricately monachal atheneum maw 
wallyballs troilites batmitzvahs projectures rhizocarpic strimming disload parvo
virus sundras hyponastically disclamations enlivening copping uprated planimetri
cal fiancee underlayments replaced humbugger counterbracing hypophysectomy overb
leached pleurae pinkoes hairifs disappearance jarks defrauder northward captives
 basement getting gallized theriomorphisms psychophysics attuiting totanus unpot
ted revegetates antimutagens sitter
"""

print("Está no texto" if texto.find("exemplo") else "Não está")
fim = time.time()
print(f"O tempo para achar a palavra no texto foi {fim-inicio}")
```

## Exercício 3:

Implemente o algoritmo de Boyer-Moore em Python. Utilize-o para encontrar a palavra "informação" em um texto em português.

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
## Exercício 4: 

Compare a eficiência do algoritmo de Boyer-Moore com o algoritmo de força bruta implementando um contador de comparações de caracteres para ambos.

```py
import time 

inicio01 = time.time()

texto = """
sufflate degenerated chrism reformism unclearest coonties pessary hepatopancreas
es vitrifactures terakihi paralinguistic hagdowns unsifted buzzards worthlessly 
bourgeoises induplicated epidemicity daughters sharesmen upstandingness matellas
se landslide drowning anteceded forslacking foresails obsessor bravely keavie mo
nishes querier marlingspike noticeable temporisings paramnesia freezingly coadmi
tting koodoo subprograms ginzo dolomitization scrawninesses sheath computerized 
empeaching reciprocant discord sawyer chloritisations untractableness untiring e
xemplo backfires incrusts regenerates haywire intricately monachal atheneum maw 
wallyballs troilites batmitzvahs projectures rhizocarpic strimming disload parvo
virus sundras hyponastically disclamations enlivening copping uprated planimetri
cal fiancee underlayments replaced humbugger counterbracing hypophysectomy overb
leached pleurae pinkoes hairifs disappearance jarks defrauder northward captives
 basement getting gallized theriomorphisms psychophysics attuiting totanus unpot
ted revegetates antimutagens sitter
"""

print("Está no texto" if texto.find("exemplo") else "Não está")
fim01 = time.time()

tempo01 = fim01-inicio01

print(f"O tempo para achar a palavra no texto foi {fim01-inicio01}")


inicio02 = time.time()

texto = """
Como vimos, os sistemas de informação possuem diferentes níveis e funcionalidades. Por isso, é evidente que esses softwares ajudam a empresa a funcionarem de maneira mais adequada.

Por meio da adoção desses sistemas, o gestor consegue reunir uma série de informações importantes, que podem impactar tanto no atendimento aos clientes quanto nos processos internos.

Além disso, a obtenção desses dados permite que o gestor ou o empreendedor analise os dados e interprete-os.

Dessa forma, as informações podem ser usadas para a tomada de decisões estratégica, controlando as informações e os dados e assegurando que a empresa esteja funcionando com o máximo de eficiência.
"""

print("Está no texto" if texto.find("informação") else "Não está")

fim02 = time.time()

tempo02 = fim02-inicio02

print(f"O tempo para achar a palavra no texto foi {fim02-inicio02}")

print(f"A diferença de tempo entre os dois textos foi de {tempo02-tempo01}")
```

## Exercício 5: 

Modifique o algoritmo de Boyer-Moore para tratar casos de textos e padrões em alfabetos não latinos, por exemplo, em caracteres cirílicos.

```py

```
## Exercício 6:

Crie um algoritmo que utilize o Boyer-Moore para encontrar todas as ocorrências não sobrepostas de um padrão em um texto e retorne as posições iniciais dessas ocorrências.

```py

```

## Exercício 7:

Implemente uma função em Python que utilize o algoritmo de Boyer-Moore para verificar se uma palavra é parte de qualquer entrada de uma lista de strings.

```py

```

## Exercício 8: 

Desenvolva um script que use o algoritmo de Boyer-Moore para encontrar e destacar todas as ocorrências de uma lista de palavras em um texto.

```py

```

## Exercício 9:

Modifique o algoritmo de Boyer-Moore para fornecer um feedback sobre a presença de um padrão em um texto, indicando não apenas a posição da primeira ocorrência, mas também quantas vezes o padrão foi encontrado.

```py

```

## Exercício 10:

Implemente uma versão do algoritmo de Boyer-Moore que seja insensível a maiúsculas e minúsculas durante a busca de um padrão em um texto.

```py

```