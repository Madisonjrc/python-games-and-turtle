from turtle import*
from math import*
correct=False
while(correct==False):
    a=int(input("Enter A Number (Side A)"))
    b=int(input("Enter A Number (Side B)"))
    c=int(input("Enter A Number(Side C)"))
    if (a+b>c and a+c>b and b+c>a):
        print("Yes this will make a triangle")
        correct=True
    else:
        print("ERROR This DOESN'T make a Triangle.Try Again.")
A=acos((pow(a,2)-pow(b,2)-pow(c,2))/(-2*b*c))
B=acos((pow(b,2)-pow(a,2)-pow(c,2))/(-2*a*c))
A=degrees(A)
B=degrees(B)
C=180-(A+B)
xnow=xcor()
ynow=ycor()
forward(a/2)
write(a)
goto(xnow,ynow)
forward(a)
write("A%.0f"%A)
left(180-C)
xnow=xcor()
ynow=ycor()
forward(b/2)
write(b)
goto(xnow,ynow)
forward(b)
write("B%.0f"%B)
left(180-A)
xnow=xcor()
ynow=ycor()
forward(c/2)
write(c)
goto(xnow,ynow)
forward(c)
write("C%.0f"%C)
left(180-B)
print("The angles are A:",A,"B:",B,"C",C)
exitonclick()

