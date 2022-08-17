from tkinter import*
myTK = Tk()
c = Canvas(myTK, width = 600, height = 400)
c.pack()
rowsize = colomnsise = 100
rows, caulums = 4, 6
array_2D = []
for i in range(rows):
    array_2D.append([])
    for j in range(caulums):
        x, y = j*colomnsise, i*rowsize
        rect= c.create_rectangle(x, y, x + colomnsise, y + rowsize)
        array_2D[i].append(rect)
for i in range(rows):
    for j in range(caulums):
        if (i+j)%2 == 0:
            c.itemconfig(array_2D[i][j], fill = 'black')
        else:
            c.itemconfig(array_2D[i][j], fill = 'white')
myTK.update
