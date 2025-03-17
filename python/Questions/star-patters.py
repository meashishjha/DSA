'''
Pattern 10

*
**
***
****
***
**
*
'''
def pattern10(rows):
    for row in range (1, 2* rows):
        if row <= rows:
            print("*" * row)
        else:
            print("*" * (2* rows - row))

#pattern10(5)

'''
Pattern 11

1
01
101
0101
10101

'''
def pattern11(rows):
    start = 1
    for row in range (1, rows + 1):
        if row % 2 == 0:
            start = 0
        else:
            start = 1

        for column in range(row):
            print(start, end="")
            start = 1 - start
        print("")

#pattern11(5)

'''
Pattern 12

1      1
12    21
123  321
12344321


'''
def pattern12(rows):
    for row in range (1, rows + 1):
        for column in range(row):
            print(column + 1, end="")

        print(" " * 2*(rows - row), end = "")

        for column in range(row,0,-1):
            print(column, end="")

        print("")

pattern12(5)