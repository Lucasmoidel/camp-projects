from tkinter import*
import time

tk = Tk()
tk.title("Tic-Tac-Toe")
canvas = Canvas(tk, width = 600, height = 600, bg = 'white')
canvas.pack()
board = [[0] * 3 for i in range(3)]
gameover = False
player = 1 
def markBoard(i, j):
    global board, player
    if board[i][j] == 0:
        board[i][j] = player
        if (player == 1):
            player = 2
        else:
            player = 1
def drawGrid():
    canvas.create_line(200, 0, 200, 600)
    canvas.create_line(400, 0, 400, 600)
    canvas.create_line(0, 200, 600, 200)
    canvas.create_line(0, 400, 600, 400)
def findAndMark(event):
    x = event.x
    y = event.y
    i = j = 0
    if (x < 200):
        j = 0
    elif (x < 400):
        j = 1
    else:
        j = 2
    if (y < 200):
        i = 0
    elif (y < 400):
        i = 1
    else:
        i = 2
    markBoard(i, j)
def updateBoard():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                drawO(i, j)
            elif board[i][j] == 2:
                drawX(i, j)
def drawX(i, j):
    left = j*200
    top = i*200
    right = left + 200
    bottom = top + 200
    canvas.create_line(left, top, right, bottom)
    canvas.create_line(right, top, left, bottom)
def drawO(i, j):
    left = j*200
    top = i*200
    right = left + 200
    bottom = top + 200
    canvas.create_oval(left, top, right, bottom)
drawGrid()
def isGameOver():
        tl = board[0][0]
        tc = board[0][1]
        tr = board[0][2]
        cl = board[1][0]
        cc = board[1][1]
        cr = board[1][2]
        bl = board[2][0]
        bc = board[2][1]
        br = board[2][2]
        if (tl != 0 and tl == tc and tc == tr):
            canvas.create_line(0, 100, 600, 100, width = 10)
            return True
        if (cl != 0 and cl == cc and cc == cr): # middle row
            canvas.create_line(0, 300, 600, 300, width = 10)
            return True
        if (bl != 0 and bl == bc and bc == br): # bottom row
            canvas.create_line(0, 500, 600, 500, width = 10)
            return True

        #CHECK COLUMNS
        if (tl != 0 and tl == cl and cl == bl): # left column
            canvas.create_line(100, 0, 100, 600, width = 10)
            return True 
        if (tc != 0 and tc == cc and cc == bc): # middle column
            canvas.create_line(300, 0, 300, 600, width = 10)
            return True
        if (tr != 0 and tr == cr and cr == br): # right colum
            canvas.create_line(500, 0, 500, 600, width = 10)
            return True

        #CHECK DIAGONALS
        if (tl != 0 and tl == cc and cc == br): # left-right diagona
            canvas.create_line(0, 0, 600, 600, width = 10)
            return True
        if (tr != 0 and tr == cc and cc == bl): # right-left diagonal
            canvas.create_line(600, 0, 0, 600, width = 10) 
            return True
        return False
canvas.bind("<Button-1>", findAndMark)
while not gameover:
    updateBoard()
    gameover = isGameOver()
    tk.update()
time.sleep(.5)
