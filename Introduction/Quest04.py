'''
Qual mês é?
Meses podem ser identificados por números ou pelos próprio nome. Dado um valor inteiro m
 identificando um mês, indique o nome deste mês do ano.

Entrada
A entrada contém uma linha com um valor inteiro 1≤m≤12
.

Saída
O nome do mês indicado pelo número lido, por extenso e com a primeira letra maiúscula. Use apenas caracteres ASCII.
'''
entrada=int(input())
mes = {1:'Janeiro',2:'Fevereiro',3:'Marco',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
print(mes[entrada])
