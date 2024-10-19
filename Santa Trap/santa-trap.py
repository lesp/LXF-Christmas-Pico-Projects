from machine import Pin, PWM
import time

pir_sensor = Pin(15, Pin.IN)
led = Pin(16, Pin.OUT)
buzzer = PWM(Pin(17))

melody = [659, 659, 659, 659, 659, 659, 659, 784, 523, 587, 659]
durations = [0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.3, 0.3, 0.6]

def play_jingle_bells():
    for note, duration in zip(melody, durations):
        if note == 0:
            time.sleep(duration)
        else:
            buzzer.freq(note)
            buzzer.duty_u16(30000)
            time.sleep(duration)
        buzzer.duty_u16(0)
        time.sleep(0.005)

while True:
    if pir_sensor.value() == 1:
        print("Santa detected!")
        for i in range(5):
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
        for i in range(3):
            play_jingle_bells()
            time.sleep(0.1)

    time.sleep(0.1)
