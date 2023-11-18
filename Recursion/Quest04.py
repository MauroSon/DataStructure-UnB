'''
Monocarp is playing a computer game. Now he wants to complete the first level of this game.

A level is a rectangular grid of 2
 rows and n
 columns. Monocarp controls a character, which starts in cell (1,1)
 — at the intersection of the 1
-st row and the 1
-st column.

Monocarp's character can move from one cell to another in one step if the cells are adjacent by side and/or corner. Formally, it is possible to move from cell (x1,y1)
 to cell (x2,y2)
 in one step if |x1−x2|≤1
 and |y1−y2|≤1
. Obviously, it is prohibited to go outside the grid.

There are traps in some cells. If Monocarp's character finds himself in such a cell, he dies, and the game ends.

To complete a level, Monocarp's character should reach cell (2,n)
 — at the intersection of row 2
 and column n
.

Help Monocarp determine if it is possible to complete the level.

The first line contains a single integer t
 (1≤t≤100
) — the number of test cases. Then the test cases follow. Each test case consists of three lines.

The first line contains a single integer n
 (3≤n≤100
) — the number of columns.

The next two lines describe the level. The i
-th of these lines describes the i
-th line of the level — the line consists of the characters '0' and '1'. The character '0' corresponds to a safe cell, the character '1' corresponds to a trap cell.

Additional constraint on the input: cells (1,1)
 and (2,n)
 are safe.

For each test case, output YES if it is possible to complete the level, and NO otherwise.
'''
def MovimentacoesFodas(mov,tam,lista):
    if mov<tam-1:
        if lista[0][mov+1]==0 or lista[1][mov+1]==0:
            return MovimentacoesFodas(mov+1,tam,lista)
        elif lista[0][mov+1]==1 and lista[1][mov+1]==1:
            return 'NO'
    else:
        return 'YES'
test_cases = int(input())
i=0
while i<test_cases:
    lista = []
    tam = int(input())
    lista.append([int(x) for x in input()])
    lista.append([int(x) for x in input()])
    print(MovimentacoesFodas(0,tam,lista))
    i+=1
