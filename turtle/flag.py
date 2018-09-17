from turtle import*
speed(0)
hoist=150
fly=hoist*1.9
hoistunion=hoist*(7/13)
flyunion=hoist*(0.76)
stripew=hoist*(1/13)
xnow=xcor()
ynow=ycor()
for i in range (2):
    forward(fly)
    right(90)
    forward(hoist)
    right(90)
for z in range (13):
    if (z%2==0):
        color("black","red")
    else:
        color("black","white")
    for s in range (2):
        pendown()
        begin_fill()
        forward(fly)
        right(90)
        forward(stripew)
        right(90)
        end_fill()
    penup()
    right(90)
    forward(stripew)
    left(90)
goto(xnow,ynow)
for u in range (2):
    color("black","blue")
    begin_fill()
    forward(flyunion)
    right(90)
    forward(hoistunion)
    right(90)
    end_fill()
def star5(length):
    for i in range(5):
        forward(length)
        right(144)
        forward(length)
        left(72)
goto(xnow+14,ynow-5)
for k in range(5):
    for r in range (5):
        penup()
        for t in range (1):
            pendown()
            begin_fill()
            color("black","white")
            star5(0.0616*hoistunion)
            penup()
            end_fill()
        forward(0.063*hoist*2)
    goto(xnow+14,ynow-5)
    right(90)
    forward(0.063*hoist*2*k)
    left(90)
exitonclick()