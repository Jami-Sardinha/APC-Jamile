from turtle import *

alice = Turtle()
alana = Turtle()

alice.color('#af9bfa', '#00534b')
lado = 150
alice.begin_fill()
alice.forward(lado)
alice.left(90)
alice.forward(lado)
alice.left(90)
alice.forward(lado)
alice.left(90)
alice.forward(lado)
alice.end_fill()


alana.color('#db7f50', '#f0ffff')
lado = 150
alana.penup()
alice.forward()
alice.left(120)
alana.forward(200)
alana.pendown()
alana.begin_fill()
alana.forward(lado)
alana.left(90)
alana.forward(lado)
alana.left(90)
alana.forward(lado)
alana.left(90)
alana.forward(lado)
alana.end_fill()

done
  