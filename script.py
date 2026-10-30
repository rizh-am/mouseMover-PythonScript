import random
import threading

from pynput import keyboard
from pynput.mouse import Controller

mouse = Controller()
stop_requested = threading.Event()

WAIT_TIME = 1


def on_key_press(key):
    stop_requested.set()


def mouse_mover():

    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    mouse.move(x, y)
    stop_requested.wait(WAIT_TIME)
    mouse.move(-x, -y)


listener = keyboard.Listener(on_press=on_key_press)
# pynput by default sets daemon = true, no need to include it to stop the listener


if __name__ == "__main__":
    listener.start()

    while not stop_requested.is_set():
        mouse_mover()
        stop_requested.wait(WAIT_TIME)

    listener.stop()  # To tell the listener to stop

    listener.join()  # To wait and check if the listener has actually stopped and joined back with the main program

    print("Program stopped")
