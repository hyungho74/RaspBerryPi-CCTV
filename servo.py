import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
servo_pin = 7 #서보모터1
servo_pin1 = 12 #서보모터2
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(servo_pin1, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50) #servo_pin의 PWM(펄스 폭)을 50으로 설정
servo1 = GPIO.PWM(servo_pin1, 50)#servo_pin1의 PWM(펄스 폭)을 50hz로 설정
servo.start(90) #서보모터1의 초기 각도를 90도로 설정
servo1.start(90) #서보모터2의 초기 각도를 90도로 설정
servo_min_duty = 3 #서보모터 최저 각도를 0으로 설정
servo_max_duty = 12 #서보모터 최고 각도를 180으로 설정
current_deg = 90

def set_servo_degree(degree):
    GPIO.setup(servo_pin, GPIO.OUT) #웹 화면에서 값을 입력받을때 입력으로 전환되기때문에 다시 출력으로 바꿔줌
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
    duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180) #웹화면에서 표기된(0~180)을 서보모터가 읽을 수 있게 3%~12%로 바꿔줌
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.setup(servo_pin, GPIO.IN) #웹 화면에서 값을 입력받아야 하기 때문에 입력으로 전환해줌
    return degree #현재 각도 return

def set_servo_degree1(degree):
    GPIO.setup(servo_pin1, GPIO.OUT) #웹 화면에서 값을 입력받을때 입력으로 전환되기때문에 다시 출력으로 바꿔줌
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
    duty1 = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180) #웹화면에서 표기된(0~180)을 서보모터가 읽을 수 있게 3%~12%로 바꿔줌
    servo1.ChangeDutyCycle(duty1)
    time.sleep(0.5)
    GPIO.setup(servo_pin1, GPIO.IN) #웹 화면에서 값을 입력받아야 하기 때문에 입력으로 전환해줌
    return degree #현재 각도 return   