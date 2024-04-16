from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle do you think will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -100
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-235, y=y)
    y += 45
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! {winning_color} was the first to cross the line! ")
                
            else:
                print(f"You have lost. {winning_color} was the first to cross the line! ")
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)
    
    
    
    
screen.exitonclick()    