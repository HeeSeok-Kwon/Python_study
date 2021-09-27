import turtle

t = turtle.Turtle()
t.shape("turtle")
radius = int(input())
t.goto(0,0)
t.circle(radius)

radius += 20
t.up()
t.goto(100,0)
t.down()
t.circle(radius)

radius += 20
t.up()
t.goto(200,0)
t.down()
t.circle(radius)
