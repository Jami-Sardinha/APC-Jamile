from turtle import *

#define a função quadrado
def quadrado():
    lado = 20
    forward(lado)
    left(90)
    forward(lado)
    left(90)
    forward(lado)
    left(90)
    forward(lado)
  
color('#ccb9ce', '#879eb2')
#executa a função quadrado

def estrela():
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    left(45)
    quadrado()
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
    left(60)
    quadrado()
   

begin_fill()
estrela()
end_fill()
penup()
left(25)
forward(250)
pendown()
begin_fill()
estrela()
end_fill()
penup()
left(25)
forward(250)
pendown()
begin_fill()
estrela()
end_fill()

done()
