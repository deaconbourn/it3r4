import time
import turtle
import random
#turtle demo
#turtling demo
turtle = turtle.Pen()

for i in range(20):
	turtle.right(45)
	turtle.forward(100)
	time.sleep(2)
	turtle.speed(0)
turtle.reset()
a =  random.randrange(20)
while True:
	for randomization in a:
		turtle.circle(20)
		turtle.forward(50)
		turtle.right(15)
	


