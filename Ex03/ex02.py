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