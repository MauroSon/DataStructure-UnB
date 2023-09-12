'''
Triângulo de Pascal I
Implemente a função triangulo, que recebe um número inteiro n e retorna todas linhas menores e iguais a n do triângulo de Pascal em uma lista.

Entrada da Função
Um número inteiro n>=0.

Saída da Função
Uma lista com todas linhas menores e iguais a n do triângulo de Pascal
'''
def triangulo(n):
    lista = [[1],[1,1]]
    cont=1
    if n>2:
        while cont<n-1:
            j=0
            k=1
            tamanho=(len(lista)-1)
            lista.append([1])
            while len(lista[tamanho+1])<len(lista[tamanho]):
                lista[tamanho+1].append(lista[tamanho][j]+lista[tamanho][k])
                k+=1
                j+=1
            lista[len(lista)-1].append(1)
            cont+=1
        return lista
    elif n==1:
        return [[1]]
    elif n==2:
        return lista
    return []
