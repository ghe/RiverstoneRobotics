# VEX IQ Python-Project
import sys
import vexiq

#region config
motor_5 = vexiq.Motor(5)
color_6 = vexiq.ColorSensor(6) # hue
#endregion config
color_6.set_grayscale_mode(True)


while True:
    motor_5.run_to_position(100, color_6.grayscale())
