'''
Frequência - Caracteres
Implemente a função frequencia, que recebe uma mensagem e retorna o caracter mais comum dessa mensagem. Em caso de empate, retorne o primeiro caracter mais frequente

Entrada:
Sequência de caracteres em uma linha.

Saída:
O caracter com maior frequência
'''
def frequencia(str_input):
    placeholder=''
    maior=0
    letraM=''
    for elem in str_input:
        if elem not in placeholder:
            placeholder+=elem
    for elem in placeholder:
        if str_input.count(elem)>maior:
            maior=str_input.count(elem)
            letraM=elem
    return letraM
