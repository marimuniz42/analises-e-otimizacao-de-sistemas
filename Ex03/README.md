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
cal fiancee underlayments replaced humbugger exemplo counterbracing hypophysectomy overb
leached pleurae pinkoes hairifs disappearance jarks defrauder northward captives
 basement getting gallized theriomorphisms psychophysics attuiting totanus unpot
ted revegetates antimutagens sitter
"""

if (index_palavra := texto.find("exemplo")) != -1:
    print(f"Está no texto em {index_palavra}")
else:
    print("Não está")
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
 basement getting gallized theriomorphisms exemplo psychophysics attuiting totanus unpot
ted revegetates antimutagens sitter
"""

if (index_palavra := texto.find("exemplo")) != -1:
    print(f"Está no texto em {index_palavra}")
else:
    print("Não está")
fim = time.time()
print(f"O tempo para achar a palavra no texto foi {fim-inicio}")
```

## Exercício 3:

Implemente o algoritmo de Boyer-Moore em Python. Utilize-o para encontrar a palavra "informação" em um texto em português.

```py
texto = """
Como vimos, os sistemas de informação possuem diferentes níveis e funcionalidades. Por isso, é evidente que esses softwares ajudam a empresa a funcionarem de maneira mais adequada.

Por meio da adoção desses sistemas, o gestor consegue reunir uma série de informações importantes, que podem impactar tanto no atendimento aos clientes quanto nos processos internos.

Além disso, a obtenção desses dados permite que o gestor ou o empreendedor analise os dados e interprete-os.

Dessa forma, as informações podem ser usadas para a tomada de decisões estratégica, controlando as informações e os dados e assegurando que a empresa esteja funcionando com o máximo de eficiência.
"""

print("Está no texto" if texto.find("informação") else "Não está")
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

if (index_palavra := texto.find("exemplo")) != -1:
    print(f"Está no texto em {index_palavra}")
else:
    print("Não está")

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
texto = """
Улучшить английский язык. Я достаточно хорошо говорю на английском, но, если я хочу устроиться работу в международную компанию, моего уровня будет недостаточно. Мне нужно будет пройти дополнительные курсы бизнес-английского и получить сертификат.
"""

print("Está no texto" if texto.find("английский") else "Não está")
```
## Exercício 6:

Crie um algoritmo que utilize o Boyer-Moore para encontrar todas as ocorrências não sobrepostas de um padrão em um texto e retorne as posições iniciais dessas ocorrências.

```py
texto = """
Улучшить английский язык. Я достаточно хорошо говорю на английском, но, если я хочу устроиться работу в международную компанию, английский моего уровня будет недостаточно. Мне нужно будет пройти дополнительные курсы бизнес-английского и получить сертификат.
"""


if number_of_times := texto.count("английский"):
    print(f"Está no texto {number_of_times} vezes")
    posicao = texto.find("английский")
    print(f"Primeira ocorrência é em {posicao}")
else: 
    print("Não está no texto")
```

## Exercício 7:

Implemente uma função em Python que utilize o algoritmo de Boyer-Moore para verificar se uma palavra é parte de qualquer entrada de uma lista de strings.

```py
import re

palavra = input("Digite uma palavra de entrada: ")

outras_palavras = [ i for i in input("Digite outras palavras separadas por espaço: ").split()] 

esta_no_texto = lambda expressao: re.search(f"^{palavra}",expressao)

array = filter(esta_no_texto,outras_palavras)

array_len = list(array)

print("Tem na lista de palavras" if len(array_len) > 0 else "Não tem na lista de palavras")
```

## Exercício 8: 

Desenvolva um script que use o algoritmo de Boyer-Moore para encontrar e destacar todas as ocorrências de uma lista de palavras em um texto.

```py
import re

texto = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""

lista_de_palavras = ["voluptatem","ut","dolorem","quae","quidem"]

for palavra in lista_de_palavras:
    if number_of_times := len(re.findall(palavra,texto)):
        print(f"{palavra} está no texto {number_of_times} vezes")
    else:
        print(f"{palavra} não está no texto")
```

## Exercício 9:

Modifique o algoritmo de Boyer-Moore para fornecer um feedback sobre a presença de um padrão em um texto, indicando não apenas a posição da primeira ocorrência, mas também quantas vezes o padrão foi encontrado.

```py
import re

texto = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""

lista_de_palavras = ["voluptatem","ut","dolorem","quae","quidem"]

for palavra in lista_de_palavras:
    if number_of_times := len(re.findall(palavra,texto)):
        print(f"{palavra} está no texto {number_of_times} vezes")
    else:
        print(f"{palavra} não está no texto")
```

## Exercício 10:

Implemente uma versão do algoritmo de Boyer-Moore que seja insensível a maiúsculas e minúsculas durante a busca de um padrão em um texto.

```py
import re

texto = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""

texto = texto.upper()

lista_de_palavras = ["voluptatem","ut","dolorem","quae","quidem"]

for palavra in lista_de_palavras:
    if number_of_times := len(re.findall(palavra.upper(),texto)):
        print(f"{palavra} está no texto {number_of_times} vezes")
    else:
        print(f"{palavra} não está no texto")
```