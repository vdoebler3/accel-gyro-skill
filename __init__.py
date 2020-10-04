from mycroft import MycroftSkill, intent_file_handler
import time
import board
import busio
import adafruit_mpu6050
import RPi.GPIO as GPIO

class AccelGyro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gyro.accel.intent')
    def handle_gyro_accel(self, message):
        self.speak_dialog('gyro.accel')
        i2c = busio.I2C(board.SCL, board.SDA)
        mpu = adafruit_mpu6050.MPU6050(i2c)
        while True:
            print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
            print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
            print("Temperature: %.2f C"%mpu.temperature)
            print("")
            time.sleep(1)

def create_skill():
    return AccelGyro()

