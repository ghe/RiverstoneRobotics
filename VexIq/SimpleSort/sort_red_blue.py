# VEX IQ Python-Project
import sys
import vexiq

#region config
motor_1 = vexiq.Motor(1)
color_2 = vexiq.ColorSensor(2) # hue
#endregion config
red = (48,40,44,128)
blue = (11,27,130,137)

color_2.led_on()
print("reading")
sys.sleep(3)
initial = color_2.raw_color()
print("initial:", initial)

def close(color):
    measurement = color_2.raw_color()
    thresholds = (20,25,50,25)
    for i in range(4):
        diff = abs(color[i] - measurement[i])
        if diff > thresholds[i]:
            #print(measurement, diff, thresholds[i])
            #sys.sleep(1)
            return False
    print("hit!", measurement)
    return True

print("watching...")
while True:
    if close(blue):
        motor_1.run(100, 100, True)
        sys.sleep(1)
        motor_1.run(-10, 100, True)
        sys.sleep(2)
    if close(red):
        motor_1.run(-100, 100, True)
        sys.sleep(1)
        motor_1.run(10, 100, True)
        sys.sleep(2)
