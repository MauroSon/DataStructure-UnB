'''
Can you remember the problem that I discussed in the earlier classes?

If not, do not worry, read it now carefully.

One day, coco-cola offered a special campaign. If you return three empty bottles to the shop, you will get a full bottle of coco-cola to drink. If you have n empty bottles right in your hand, how many full bottles of coco-cola can you drink?

There will be at most 10 test cases, each containing a single line with an integer n (0 < n < 101). The input terminates with n = 0, which should not be processed.

For each test case, print the number of full bottles of coco-cola that you can drink.
'''
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
