import turtle as t
data1=[-30,70]
data2=[30,70]
data3=[-30,0]
data4=[30,0]
data5=[-30,-70]
data6=[30,-70]
data7=[0,35]
data8=[-55,65]
data9=[60,-50]
data10=[-60,85]
data11=[55,-85]
data12=[-75,120]
def fangkuai(x,y): #画七个小方块
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(60)
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(20)
        t.left(60)
        t.forward(20)
        t.left(120)
    t.end_fill()
    t.hideturtle()
def fangkuaixiao(x, y):#画两个小方块
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(60)
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(10)
        t.left(60)
        t.forward(10)
        t.left(120)
    t.end_fill()
    
def num(a,b):
    text="7"
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.write(text, font=("Arial", 24, "bold"))
def framework(m, n):
    t.penup()
    t.goto(m, n)
    t.pendown()
    t.color("red")
    t.pensize(1)
    t.seth(0)
    for i in range(2):
        t.forward(150)
        t.right(90)
        t.forward(200)
        t.right(90)
t.speed(0)
t.hideturtle()
fangkuai(data1[0],data1[1])
fangkuai(data2[0],data2[1])
fangkuai(data3[0],data3[1])
fangkuai(data4[0],data4[1])
fangkuai(data5[0],data5[1])
fangkuai(data6[0],data6[1])
fangkuai(data7[0],data7[1])
fangkuaixiao(data8[0],data8[1])
fangkuaixiao(data9[0],data9[1])
num(data10[0],data10[1])
num(data11[0],data11[1])
framework(data12[0],data12[1])
