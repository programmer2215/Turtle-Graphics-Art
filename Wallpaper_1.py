from turtle import *
hideturtle()

a = 1
speed(0)
bgcolor("#121212")
color("#2cf5d0") #ff2f00 for RED

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