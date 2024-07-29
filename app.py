import pyautogui as pg
import numpy as np
import time

grid = []

while True:
    row = list(input('Row: '))
    number = []

    for i in row:
        number.append(int(i))
    grid.append(number)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Added')

time.sleep(5)



def expected(x, y, n):          # (row, col, number)
    for i in range(0,9):
        if grid[i][x] == n and i != y:
            return False
        
    for i in range(0,9):
        if grid[y][i] == n and i != x:
            return False
            
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3
    for X in range(x1, x1 + 3):
        for Y in range(y1, y1 + 3):
            if grid[Y][X] == n:
                return False
        
    return True             #True, if no condition is passing 
    
def display(g):
    final = []
    my_final = []
    for i in range(9):
        final.append(g[i])

    for row in final:
        for num in row:
            my_final.append(str(num))       # convert to str, as pyautogui only understand str

    reg = []
    for num in my_final:
        pg.press(num)
        pg.hotkey('right')
        reg.append(num)
        if len(reg) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def play():                                 # Backtracking Block
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if expected(x, y, n):
                        grid[y][x] = n
                        play()              # recursion occuring
                        grid[y][x] = 0      #after recursion nothing works, then go back to 0
                return 
            
    display(grid)
    input('Puzzle solved... Did you like it?')

play()

