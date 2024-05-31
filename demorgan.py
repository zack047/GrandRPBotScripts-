import keyboard
import time

def press_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def main():
    while True:
        # Press 'w' for 2 seconds
        press_key('w', 2)
        
        # Press 's' for 2 seconds
        press_key('s', 2) 


              
        # Wait for 9 minutes
        time.sleep(9 * 60)

if __name__ == "__main__":
    main()
