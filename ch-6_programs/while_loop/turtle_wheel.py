import turtle

turtle.color("black")
turtle.speed(5)

counter = 0
while counter < 36:
    for i in range(10):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()