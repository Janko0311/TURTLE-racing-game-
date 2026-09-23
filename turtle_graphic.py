import turtle
from turtle import Turtle, Screen
import random


turtleColor=("red","green","blue","yellow","orange","purple")

screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")

turtleObj=[]
winner = ""
raceStart = False


def turtle_setup():
    for setUpIndex in range(len(turtleColor)):
        turtleObj.append(Turtle())
        turtleObj[setUpIndex]=Turtle(shape="turtle")
        turtleObj[setUpIndex].color(turtleColor[setUpIndex])
        turtleObj[setUpIndex].penup()
        turtleObj[setUpIndex].goto(x=-630,y=-216+setUpIndex*100)
turtle_setup()
user_input = screen.textinput(prompt="Enter your guess:",title="Make a guess.")

def turtle_race():
    global winner
    raceStart = True
    while raceStart:
        for raceIndex in range(len(turtleColor)):
            if not turtleObj[raceIndex].xcor() >= 645 and raceStart==True:
                turtleObj[raceIndex].forward(random.randint(0,20))

            else:
                winner=turtleColor[raceIndex]


                raceStart = False





while user_input != "" and winner =="":
    turtle_race()

if user_input == winner:
    print("Congratulations! You guessed the winner!")
else:
    print("the winner is {}".format(winner))
    turtle.bye()

