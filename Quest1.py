'''
Divisores Primos
Implemente a função divisores, que recebe um número inteiro e retorna todos os seus divisores inteiros (incluindo 1 e ele mesmo) em uma lista.

Entrada da Função
Um número inteiro n>0
.

Saída da Função
Uma lista com todos os divisores desse número
'''
def divisores(n):
    result=[]
    for elem in range(1,n+1):
        if n%elem==0:
            result.append(elem)
    return(result)
