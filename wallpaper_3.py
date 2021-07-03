from turtle import *
hideturtle()

a = 1
speed(0)
bgcolor("#121212")
color("#2cf5d0") #ff2f00 for RED
flag = False
def switch():
    return not flag

for i in range(100):
    
    forward(a)
    left(80)
    forward(a)
    left(80)
    forward(a)
    left(80)
    forward(a)
    if i % 20 == 0:
        flag = switch()
    if flag:
        color("#ff2f00")
    else:
        color("#2cf5d0")
    a += 2
    
mainloop()