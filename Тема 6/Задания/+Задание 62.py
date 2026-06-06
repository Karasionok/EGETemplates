# Решение


from turtle import *

screensize(50, 50)
tracer(0)
k = 5

down()
right(180)
for i in range(9):
    forward(k * 59)
    left(90)
    forward(84 * k)
    left(90)

up()
forward(18 * k)
left(90)
forward(k * 38)
right(90)
down()

for i in range(9):
    forward(120 * k)
    right(90)
    forward(99 * k)
    right(90)

up()
for x in range(-k * 20, k * 20):
    for y in range(-k * 20, k * 20):
        goto(x * k, y * k)
        dot(3)
exitonclick()




answer = 158

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))