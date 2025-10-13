from turtle import *

tracer(0)
koef = 20

x = 1
down()
forward(x + 2)
for i in range(4):
    forward(x)
    right(90)
    forward(x + 2)
right(90)
forward(2 * x)
for j in range(4):
    right(90)
    forward(3 * x - 1)
up()


for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()




answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))