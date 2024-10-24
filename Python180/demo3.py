import turtle

# Setup the screen
wn = turtle.Screen()
wn.setup(width=400, height=400)

# Create a turtle for drawing the heart
red = turtle.Turtle()

# Define the curve function
def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

# Define the heart function
def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

# Draw the heart
heart()

# Hide the turtle
red.hideturtle()

# Create a new turtle for writing text
text_turtle = turtle.Turtle()

# Position the turtle for writing text
text_turtle.penup()
text_turtle.goto(0, -180)  # Adjust the position as needed

# Write the text
text_turtle.write("Cat_😸🐈", align="center", font=("Arial", 20, "normal"))

# Hide the text turtle
text_turtle.hideturtle()

# Keep the window open
turtle.done()
