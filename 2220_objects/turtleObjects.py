import turtle

tortoise = turtle.Turtle()
otherTortoise = turtle.Turtle()
slowTortoise = turtle.Turtle()

tortoise.shape('turtle')
tortoise.speed(3)
tortoise.fd(50)

otherTortoise.color('green')
otherTortoise.shape('turtle')
otherTortoise.speed(3)
otherTortoise.left(90)
otherTortoise.fd(50)

slowTortoise.color('red')
slowTortoise.shape('turtle')
slowTortoise.speed(1)
slowTortoise.left(180)
slowTortoise.fd(50)

