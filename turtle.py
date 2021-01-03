import turtle

from random import *

#초기랜덤좌표 생성
fw=open("inputfile.txt","w")

Coordinates=[]
num = round(uniform(0, 1000),2)

def randomxy (z):
    global num
    for i in range(z):
        while num in Coordinates :
            num = round(uniform(0, 1000),2)
        Coordinates.append(num)

x=int(input("좌표수를 입력하세요"))
randomxy(z= 2 * x)
j=1
print(x,"개의 좌표")
while j <= len(Coordinates):
    print(Coordinates[j-1], Coordinates[j])
    j += 2

fw.write(str(x))
fw.write('\n')
j=1
while j<=len(Coordinates):
    fw.write(str(Coordinates[j-1])+' ')
    fw.write(str(Coordinates[j]))
    fw.write('\n')
    j+=2
fw.close()
print("--------------- \ninputfile에 저장")
#print(Coordinates)
#start_pos = 0
#end_pos = len(Coordinates)

#div = 2

#for idx in range(start_pos, end_pos + div, div):
#    out = Coordinates[start_pos:start_pos + div]
#    if out != []:
#        print (out)
#    start_pos = start_pos + div
#




#초기정점 찍는 것 보여주는 터틀 그래픽
fw=open("inputfile.txt","w")
y=int(input("좌표수를 입력하세요"))
t=turtle
q=0
t.speed(0)
t.screensize(3000,3000)
t.shape("turtle")
turtleVlist=[]
turtleElist=[]
def drawrandomxy (x):
    global q
    for i in range(x):
        t.penup()
        t.goto(round(uniform(0,1000),2), (round(uniform(0,1000),2)))
        t.pendown()
        t.circle(3)
        turtleVlist.append(t.xcor())
        turtleVlist.append(t.ycor())
        #turtleElist의 첫번째 인덱스는 0.0,
        #두 번째 인덱스 부터
        #turtleVlist의 0(x), 1(y)과 2(x), 3(y) 인덱스 거리값 저장
        #2,3과 4,5의 인덱스 거리값 저장, 4,5와 6,7의 거리값.... 이런식
        #
        p=t.distance(turtleVlist[q-2], turtleVlist[q-1])
        turtleElist.append(p)
        q+=2

drawrandomxy(y)
print("inputfile에 정점수, 값저장")
j=0
fw.write(str(y))
fw.write('\n')
j=1
while j<=len(turtleVlist):
    fw.write(str(turtleVlist[j-1])+' ')
    fw.write(str(turtleVlist[j]))
    fw.write('\n')
    j+=2
fw.close()
turtleElist.pop(0)
#turtleVlist는 정점x y좌표를 쭉 넣음 => 정점 1000개면 2000개 인덱스
#turtleElist는 정점들 사이의 거리 넣음 => 정점 1000개면 999개 인덱스



