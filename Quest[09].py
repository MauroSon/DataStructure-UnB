'''
Compressão de Strings
Johnny é um cara legal que gostava de carros e brincar com algoritmos de compressão. Ele está trabalhando em um projeto no qual tem que lidar com cadeias de caracteres extremamente grandes. O maior problema de Johnny nesse trabalho é que essas strings são grandes demais para manipular diretamente, então ele precisa de uma representação alternativa (menor) para a mesma informação. Johnny pensou em usar uma técnica bem conhecida para comprimir as strings: trocar ocorrências consecutivas de um mesmo caractere por uma única ocorrência deste mesmo caractere, seguida da quantidade de ocorrências. Neste formato, todo caractere é seguido por um inteiro positivo. Essa compressão permitiu que ele comunicasse suas strings, mas ele não consegue processá-las corretamente e agora precisa da sua ajuda para revertê-las às suas formas originais.



Entrada
A entrada é composta de uma linha contendo um inteiro N (1 ≤ N ≤ 50), seguida de N linhas distintas, cada uma com uma string codificada. É garantido que toda string tem pelo menos um caractere e está no formato comprimido, ou seja, é composto apenas por letras (maiúsculas) e dígitos.



Saı́da
Apresente as strings decodificadas, uma por linha.
'''
n = int(input())
i=0
while i<n:
    frase=''
    j=0
    l=0
    string = input()
    while l<len(string)-1:
        letra=''
        num=''
        while string[j].isalpha():
            letra+=string[j]
            j+=1
            l+=1
        while string[j].isnumeric():
            num+=string[j]
            if j<len(string)-1:
                j+=1
                l+=1
            else:
                break
        frase+=letra*int(num)
    print(frase)
    i+=1
