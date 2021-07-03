from turtle import *
hideturtle()

a = 1
speed(0)
bgcolor("#121212")
color("#ff2f00") #2cf5d0 for CYAN

for i in range(100):
    
    forward(a)
    left(80)
    forward(a)
    left(80)
    forward(a)
    left(80)
    forward(a)

    a += 2
    
mainloop()