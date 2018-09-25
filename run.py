# импорт необходимых модулей Python для работы
import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

# обозначения пинов
pinGrab = 14
pinUp = 15
pinRound = 18
pinRoundGrab = 23

# включение пинов в состояние OUT (вывода сигнала)
gp.setup(pinGrab, gp.OUT)
gp.setup(pinUp, gp.OUT)
gp.setup(pinRound, gp.OUT)
gp.setup(pinRoundGrab, gp.OUT)

# инициализация PWM (ШИМ) для каждого пина
pwmGrab = gp.PWM(pinGrab, 50)
pwmGrab.start(0)
pwmUp = gp.PWM(pinUp, 50)
pwmUp.start(0)
pwmRound = gp.PWM(pinRound, 50)
pwmRound.start(0)
pinRoundGrab = gp.PWM(pinRoundGrab, 50)
pinRoundGrab.start(0)

# функция для установления угла поворота мотора
def SetAngle(pwm, pin, angle):
    angle = angle / 18 + 2
    gp.output(pin, True)
    pwm.ChangeDutyCycle(angle)
    sleep(1)


# циклическое выполнение программы
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

# очистка пинов от значений, установленных ранее
gp.cleanup()
