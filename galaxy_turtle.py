import turtle
    
t = turtle.Turtle()
t.pencolor("blue")
t.speed("fastest")
r = 10
n = 15
for i in range(1, n + 1, 1):
    t.circle(r * i)
turtle.mainloop()