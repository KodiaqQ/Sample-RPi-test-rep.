# импорт необходимых модулей Python для работы
import RPi.GPIO as gp
from time import sleep

# установка вида подключения пинов
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
pwmRoundGrab = gp.PWM(pinRoundGrab, 50)
pwmRoundGrab.start(0)


# функция для установления угла поворота мотора
def set_angle(pwm, pin, angle):
    angle = angle / 18 + 2
    gp.output(pin, True)
    pwm.ChangeDutyCycle(angle)
    sleep(1)


if __name__ == '__main__':
    # циклическое выполнение программы
    while True:
        # опускаем захват
        set_angle(pwmUp, pinUp, 135)
        # захватываем деталь
        set_angle(pwmGrab, pinGrab, 90)
        # поднимаем захват с деталью
        set_angle(pwmUp, pinUp, 45)
        # поворот захвата вокруг центральной оси на 90 градусов
        set_angle(pwmRoundGrab, pinRoundGrab, 90)
        # поворот на 180 градусов вокруг оси робота
        set_angle(pwmRound, pinRound, 180)
        # опускаем захват
        set_angle(pwmUp, pinUp, 135)
        # разжимаем захват
        set_angle(pwmGrab, pinGrab, 0)
        # возвращаем в исходное положение
        set_angle(pwmUp, pinUp, 0)
        set_angle(pwmRoundGrab, pinRoundGrab, 0)
        set_angle(pwmRound, pinRound, 0)

    # очистка пинов от значений, установленных ранее
    gp.cleanup()
