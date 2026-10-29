from pynput import keyboard
from pynput.mouse import Controller
import threading
import random

mouse = Controller()
stop_requested = threading.Event()

WAIT_TIME = 3


def on_key_press(key):
    stop_requested.set()


def mouse_mover():

    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    mouse.move(x, y)
    stop_requested.wait(1)
    x = -x
    y = -y
    mouse.move(x, y)


listener = keyboard.Listener(on_press=on_key_press)

listener.start()


while not stop_requested.is_set():
    mouse_mover()
    stop_requested.wait(WAIT_TIME)
