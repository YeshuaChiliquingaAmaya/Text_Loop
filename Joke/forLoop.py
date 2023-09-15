import pyautogui as gui
import time
import keyboard

message = input("Enter the message: ")
number_value = input("Enter the number:")

time.sleep(2)

for i in range(int(number_value)):
    keyboard.write(message)
    keyboard.press_and_release('Enter')
