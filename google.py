import turtle as t

a=t.Turtle()
a.speed(100)
a.color("red")
a1=t.Turtle()
a1.speed(100)
a1.color("green")
a1.left(180)
a2=t.Turtle()
a2.speed(100)
a2.color("blue")
a2.left(270)
a3=t.Turtle()
a3.speed(100)
a3.color("orange")
a3.left(90)
for x in range(1,1000):
    
    a.forward(x%30)
    a.left(x%30)
    a1.forward(x%30)
    a1.left(x%30)
    a2.forward(x%30)
    a2.left(x%30)
    a3.forward(x%30)
    a3.left(x%30)

#for x in range(1,1000):
    
    

    
t.done()

