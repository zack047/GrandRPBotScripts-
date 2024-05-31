
import keyboard
import time

def hold_and_release_key(key, hold_duration, release_duration):
    keyboard.press(key)
    time.sleep(hold_duration)
    keyboard.release(key)
    time.sleep(release_duration)

def main():
    try:
        while True:
            hold_and_release_key('e', 10, 5)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
