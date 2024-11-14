import turtle as t
t1=t.Turtle()
t2=t.Turtle()
t1.speed(0)
t1.hideturtle()
t2.speed(0)
t2.hideturtle()
name=input("请输入你的姓名:")
community=input("请输入你参加的社团:")
qq=input("请输入你的QQ号:")
slogan=input("请输入你的个性签名:")
data1=[-150,-100,"white"]
data2=[-150,-200,"#0083cb"]
data3=[110,-100,name,"华文行楷",60]
data4=[-145,0,community,"方正舒体",30]
data5=[150,-140,qq,"方正舒体",30]
data6=[100,-160,slogan,"方正舒体",20]
def juxing(x,y,z):#画背景 
    t1.pencolor("black")
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.seth(0)
    t1.begin_fill()
    t1.fillcolor(z)
    t1.forward(500)
    t1.left(90)
    t1.forward(150)
    t1.left(90)
    t1.forward(500)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.end_fill()
def xiangqing(x1,y1,c,t,z): #文字部分z字体大小 c输入内容
    t2.pencolor("black")#t为字体
    t2.penup()
    t2.goto(x1,y1)
    t2.pendown()
    t2.write(c,font=(t,z,"normal"))
    #align="center"文本中心对齐
    #font=("Arial", 16, "normal")字体，大小，样式


juxing(data1[0],data1[1],data1[2])
juxing(data2[0],data2[1],data2[2])
xiangqing(data3[0],data3[1],data3[2],data3[3],data3[4])#姓名
xiangqing(data4[0],data4[1],data4[2],data4[3],data4[4])#社团
xiangqing(data5[0],data5[1],data5[2],data5[3],data5[4])#QQ
xiangqing(data6[0],data6[1],data6[2],data6[3],data6[4])#个签
