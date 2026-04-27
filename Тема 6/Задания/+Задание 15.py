# Решение

from turtle import *

tracer(0)
k = 40

down()
for i in range(4):
    forward(k * 14)
    right(90)
for i in range(5):
    forward(5 * k)
    right(45)
up()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
exitonclick()


answer = 59

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 15, answer, '093f65e080a295f8076b1c5722a46aa2'))