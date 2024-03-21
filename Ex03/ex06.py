texto = """
Улучшить английский язык. Я достаточно хорошо говорю на английском, но, если я хочу устроиться работу в международную компанию, английский моего уровня будет недостаточно. Мне нужно будет пройти дополнительные курсы бизнес-английского и получить сертификат.
"""


if number_of_times := texto.count("английский"):
    print(f"Está no texto {number_of_times} vezes")
    posicao = texto.find("английский")
    print(f"Primeira ocorrência é em {posicao}")
else: 
    print("Não está no texto")