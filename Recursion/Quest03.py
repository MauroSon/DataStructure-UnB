'''
Vasily has a number a, which he wants to turn into a number b. For this purpose, he can do two types of operations:

multiply the current number by 2 (that is, replace the number x by 2·x);
append the digit 1 to the right of current number (that is, replace the number x by 10·x + 1).
You need to help Vasily to transform the number a into the number b using only the operations described above, or find that it is impossible.

Note that in this task you are not required to minimize the number of operations. It suffices to find any way to transform a into b.

The first line contains two positive integers a and b (1 ≤ a < b ≤ 109) — the number which Vasily has and the number he wants to have.

If there is no way to get b from a, print "NO" (without quotes).

Otherwise print three lines. On the first line print "YES" (without quotes). The second line should contain single integer k — the length of the transformation sequence. On the third line print the sequence of transformations x1, x2, ..., xk, where:

x1 should be equal to a,
xk should be equal to b,
xi should be obtained from xi - 1 using any of two described operations (1 < i ≤ k).
If there are multiple answers, print any of them.
'''
def transform(a,b,lista):
    if b==a:
        return ['YES',len(lista),lista]
    else:
        if b%2==0 and b>a:    
            lista.insert(0,b//2)
            return transform(a,b//2,lista)
        elif (b-1)%10==0 and b>a:
            lista.insert(0,(b-1)//10)
            return transform(a,(b-1)//10,lista)
        else:
            return 'NO'
a,b = map(int,input().split())
result = transform(a,b,[b])
if result=='NO':
    print('NO')
else:
    print(result[0])
    print(result[1])
    print(*result[2])
