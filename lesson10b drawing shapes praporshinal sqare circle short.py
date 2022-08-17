import turtle
T = turtle.Turtle()
T.speed(0)
r = 5
wf = 250
T.pencolor("red")
T.left(90)
for i in range (4):
    r = 5
    wf = 250
    for i in range(5):
        for i in range(r):
            for i in range(4):
                T.forward (50)
                T.rt(90)
            T.forward (50)
    
        T.rt(90)
        T.fd(50)
        T.rt(90)
        r=r-1
        print(r)
        print(wf)
        T.fd(wf)
        wf=wf-50
        T.lt(180)
    T.lt(90)
    T.fd(200)
#################
#T.lt(180)
#T.fd(50)
#T.rt(90)
#T.fd(200)

turtle.done()
