import threading
light = threading.Event()
print(light.is_set())
print(light.set())
print(light.is_set())
print(light.clear())
print(light.is_set())
print(light.wait(3))