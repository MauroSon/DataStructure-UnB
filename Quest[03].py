'''
Lesma

Um dos professores desta disciplina possui como hobby criar dataset dos mais diversos tipos. Datasets são conjuntos de dados X
 normalmente estruturados em tabelas que contém L
 pares de dados. 

O último dataset gerado por esse professor misterioso é sobre lesmas. A responsabilidade de capturar lesmas velozes não é uma tarefa trivial de ser resolvida, uma vez que todas as lesmas são muito lentas. Neste dataset, cada lesma é rotulada em três níveis de acordo com sua velocidade, sendo elas:

Classe 1: Velocidade menor que 10 cm/h.
Classe 2: Velocidade maior ou igual 10 cm/h e menor que 20 cm/h.
Classe 3: Velocidade maior ou igual a 20 cm/h.
Diante do exposto, vamos ajudar o nosso querido professor a implementar um programa que a lesma mais veloz de cada classe em um grupo de lesmas.



Entrada:
A primeira linha (L) representa a quantidade de lesmas, sendo que (1≤L≤100
). Cada linha subsequente apresenta as velocidades Vi
 de cada lesma, sendo estes inteiros onde (1≤Vi≤50
).



Saída:
Para cada classe, apresente a lesma com maior velocidade. Se uma determina classe não apresentar amostras, retornar o valor zero.
'''
n = int(input())
i = 0
classes = {'classe1':[0],'classe2':[0],'classe3':[0]}
while i<n:
    lesma = int(input())
    if lesma<10:
        classes['classe1'].append(lesma)
    elif lesma<20:
        classes['classe2'].append(lesma)
    else:
        classes['classe3'].append(lesma)
    i+=1
for elem in classes:
    print(max(classes[elem]),end=' ')
