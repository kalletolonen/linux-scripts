import pyautogui
import random
import time

def move_mouse_randomly(distance):
    x_offset = random.randint(-distance, distance)
    y_offset = random.randint(-distance, distance)
    current_x, current_y = pyautogui.position()
    new_x = current_x + x_offset
    new_y = current_y + y_offset
    pyautogui.moveTo(new_x, new_y, duration=0.5)

def main():
    try:
        while True:
            move_mouse_randomly(20)
            time.sleep(30)
    except KeyboardInterrupt:
        print("Mouse movement stopped.")

if __name__ == "__main__":
    main()
