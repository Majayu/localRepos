"""
ITS 1801 F22 HW-03
Add the additional lines and elements to make the code run as expected
Check Blackboard for details
"""

import turtle

casper = turtle.Turtle()
piper = turtle.Turtle()
hazel = turtle.Turtle()

casper.shape("turtle")
piper.shape("triangle")
hazel.shape("classic")

piper.penup()
piper.goto(-150,0)
hazel.penup()
hazel.goto(150,0)
piper.pendown()
hazel.pendown()

# Do not change anything above this line
# Before changing anything below, commit it to a new repository in your github account
# and open it in a new browser tab, so that you can check the original line numbers

def square(turtleName,lineColor):
  turtleName.color(lineColor)
  # Inside the function square put in a for loop to draw a square with sides 50 pixels long

def triangle(turtleName,lineColor):
  turtleName.color(lineColor)
  # Inside the function triangle put in a for loop to draw a triangle with sides 50 pixels long

def circle(turtleName,lineColor):
  turtleName.color(l49ineColor)
  # Inside the function circle use a command to draw a circle with a 50 pixel radius
  # Check Python's Turtle documentation online to find the command and the right syntax


print("This program has three turtles: Piper (left), Casper (middle) and Hazel (right)")
print("Piper draws squares, Casper triangles and Hazel circles.")
choiceTurtleStr = input("Select a turtle (0) Piper (1) Casper (2) Hazel: ")
choiceColorStr = input("Select a color (0) yellow, (1) blue, (2) red: ")

# Define a list named colorList with string elements yellow, blue and red (in that order)
# Remember to use single or double quotation marks for each string
colorList = []

# Transform the color selected by the user (and stored in choiceColorStr) to an integer
choiceColorInt = 

if choiceTurtleStr == '0':
  # Draw a square using piper, with the color selected from colorList
  square(piper,  )
elif choiceTurtleStr == '1':
  # Draw a triangle using casper, with the color selected from colorList
  triangle( , )
elif choiceTurtleStr == '2':
  # Draw a circle using hazel, with the color selected from colorList
  circle( , )
else:
  print("Invalid choice, turtle should be between 0 and 2")