def drink(i,cont):
    if i==1:
        return cont
    else:
        if i==2:
            return drink(i+1,cont)
        else:
            return drink(i//3+i%3,cont+i//3)
i = int(input())
while i!=0:
    print(drink(i,0))
    i = int(input())
