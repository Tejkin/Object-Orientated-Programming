from turtle import Turtle
from random import randint


##creating turtles
bob = Turtle()
morty = Turtle()
oliv = Turtle()
sfen = Turtle()


##customising turtles
bob.color('blue')
bob.shape('turtle')

morty.color('pink')
morty.shape('turtle')

oliv.color('yellow')
oliv.shape('turtle')

sfen.color('purple')
sfen.shape('turtle')



##bringing turtles to start line
bob.penup()
bob.goto(-160,100)
bob.pendown()

morty.penup()
morty.goto(-160,70)
morty.pendown()

oliv.penup()
oliv.goto(-160, 40)
oliv.pendown()

sfen.penup()
sfen.goto(-160,10)
sfen.pendown()


##randomizing turtle movement

for movement in range(100):
    bob.forward(randint(1,5))
    morty.forward(randint(1,5))
    oliv.forward(randint(1,5))
    sfen.forward(randint(1,5))

input("Press enter to close")