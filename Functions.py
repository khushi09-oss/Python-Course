#decoraters
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper



@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())

# Import Required Library
from tkinter import *
import datetime
import time
import winsound
def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

