import turtle as t
pen = t.Turtle()
t.bgcolor('#58A399')
t.delay(8)
pen.color('#9966cc')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-60, 100)
    pen.color('red')
    ##license('Ankit_Bhaiya');
    #str1="Akit bhaiya"
    #print(pen .write(center(50))
    pen.write('Python_', font=("Comic Sans MS", 20))
txt()
pen.end_fill()
t.exitonclick()
open