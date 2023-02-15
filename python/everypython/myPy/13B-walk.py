import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up ():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()


t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right") # 사용자가 키보드의 오른쪽 방향키를 누르면 파이썬이 turn_right 함수를 호출하도록 예약
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank,"Escape")
t.listen() # 거북이 그래픽 창이 키보드 입력을 받을 수 있도록 거북이 창에 포커스를 주는 문장 
