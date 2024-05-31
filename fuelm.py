import pyautogui
import time

# Function to press and hold left mouse button for a specified duration
def press_and_hold(duration):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

# Function to perform the mouse actions
def perform_mouse_actions():
    # Press and hold left mouse button for 4.8 seconds
    press_and_hold(4.8)

    # Move the cursor 10 cm to the right
    pyautogui.moveRel(100, 0)  # Assuming 1 cm = 10 pixels, adjust as needed

    # Press and hold left mouse button for 4.8 seconds
    press_and_hold(4.8)

    # Move the cursor 10 cm to the right
    pyautogui.moveRel(100, 0)

    # Press and hold left mouse button for 4.8 seconds
    press_and_hold(4.8)

    # Move the cursor 10 cm to the right
    pyautogui.moveRel(100, 0)

    # Press and hold left mouse button for 4.8 seconds
    press_and_hold(4.8)

    # Move the cursor back to the original position
    pyautogui.moveTo(initial_position)

# Main loop
while True:
    # Store the initial mouse position
    initial_position = pyautogui.position()

    perform_mouse_actions()

    # Pause for a moment before the next iteration
    time.sleep(1)
