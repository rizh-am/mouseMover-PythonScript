from pynput.mouse import Button, Controller
import threading
import time
import random

mouse = Controller()

for i in range(10):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    mouse.move(x,y)
    print(x)
    print(y)
    time.sleep(1)
    x = x * -1
    y = y * -1
    mouse.move(x,y)
    print(x)
    print(y)



# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))

# # Set pointer position
# mouse.move(100, 100)
# time.sleep(1)
# print('Now we have moved it to {0}'.format(
#     mouse.position))
# time.sleep(1)
# mouse.move(-100,-100)

# time.sleep(1)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# # # Move pointer relative to current position
# # mouse.move(5, -5)

# # # Press and release
# # mouse.press(Button.left)
# # mouse.release(Button.left)

# # # Double click; this is different from pressing and releasing
# # # twice on macOS
# # mouse.click(Button.left, 2)

# # # Scroll two steps down
# # mouse.scroll(0, 2)