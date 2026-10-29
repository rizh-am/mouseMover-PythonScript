from pynput import keyboard

# Imports pynput keyboard
# It is a third party library that can scan your inputs

from pynput.mouse import Button, Controller

# Imports pynput mouse

import threading

# Basically, this imports multi processing. Like running two threads at once

import random

# imports the random library

mouse = Controller()
# Getting mouse control

WAIT_TIME = 3
stop_requested = threading.Event()
# Creating a shared flag between two functions


# Watcher function, this function sets the flag if there has been any inputs
def on_key_press(key):
    print(stop_requested.is_set())
    # Prints the current value of the flag. False at start
    stop_requested.set()
    # Updates the flag
    print(stop_requested.is_set())
    # displays the current value. True now


# This function moves the mouse
def mouse_mover():
    x = random.randint(
        -50, 50
    )  # generates a random number between -50 and +50 for the x and y coordinates
    y = random.randint(-50, 50)
    mouse.move(
        x, y
    )  # moves the mouse by the x and y values relative to the current position
    stop_requested.wait(
        WAIT_TIME
    )  # sets the flag if there is an input, waits 3 seconds otherwise
    # only here because I want to see the mouse move
    x = -x  # converting the values to negative
    y = -y
    mouse.move(x, y)  # moving back the cursor position


listener = keyboard.Listener(on_press=on_key_press)
# Created a listener variable that reads any keyboard input
# keyboard.Listener(on_press = _______) is basically pynput syntax
# on_key_press is the watcher function, so it calls on success

listener.start()
# Actually starts the listener


# Loop runs while the Flag is false
# When the listener catches any input, it calls the watcher, and the flag is updated
# When the flag is updated, because it is a threading Event, the value gets updated for the loop,
# and the loop stops
# simple as that
while stop_requested.is_set() is not True:
    mouse_mover()
    # calls the mover
    stop_requested.wait(WAIT_TIME)
# This is a dynamic wait
# basically means, wait until stop_requested (the shared flag variable) has value, or until the time is up
# once the wait time is over the loop runs again, moving the mouse, and waiting for 3 seconds because of the dynamic wait
