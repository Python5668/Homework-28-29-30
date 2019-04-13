from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

led = LED(23)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn LED on"
    else:
        led.on()
        ledButton["text"] = "Turn LED off"

ledButton = Button(win, text = "Turn LED on", font = myFont, command = ledToggle,
                   bg = "bisque2", height = 1, width = 24)
ledButton.grid(row = 0, column = 1)
