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