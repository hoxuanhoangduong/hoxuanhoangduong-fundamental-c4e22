from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']


for n in range(6):
    color("black",colors[n])
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(100)

mainloop() 