import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
pinGrab = 14
pinUp = 15
pinRound = 18
pinRoundGrab = 23

# enable pins
gp.setup(pinGrab, gp.OUT)
gp.setup(pinUp, gp.OUT)
gp.setup(pinRound, gp.OUT)
gp.setup(pinRoundGrab, gp.OUT)

# enable PWM
pwmGrab = gp.PWM(pinGrab, 50)
pwmGrab.start(0)
pwmUp = gp.PWM(pinUp, 50)
pwmUp.start(0)
pwmRound = gp.PWM(pinRound, 50)
pwmRound.start(0)
pinRoundGrab = gp.PWM(pinRoundGrab, 50)
pinRoundGrab.start(0)

# function for motor move by angle change
def SetAngle(pwm, pin, angle):
    angle = angle / 18 + 2
    gp.output(pin, True)
    pwm.ChangeDutyCycle(angle)
    sleep(1)

    
while True:
    # опускаем захват
    SetAngle(pwmUp, pinUp, 135)
    # захватываем деталь
    SetAngle(pwmGrab, pinGrab, 90)
    # поднимаем захват с деталью
    SetAngle(pwmUp, pinUp, 45)
    # поворот захвата вокруг центральной оси на 90 градусов
    SetAngle(pwmRoundGrab, pinRoundGrab, 90)
    # поворот на 180 градусов вокруг оси робота
    SetAngle(pwmRound, pinRound, 180)
    # опускаем захват
    SetAngle(pwmUp, pinUp, 135)
    # разжимаем захват
    SetAngle(pwmGrab, pinGrab, 0)
    # возвращаем в исходное положение
    SetAngle(pwmUp, pinUp, 0)
    SetAngle(pwmRoundGrab, pinRoundGrab, 0)
    SetAngle(pwmRound, pinRound, 0)
    
gp.cleanup()
