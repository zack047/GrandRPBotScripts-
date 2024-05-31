import keyboard
import time

def spam_press_key_e(duration, spam_interval):
    start_time = time.time()

    while time.time() - start_time < duration:
        keyboard.press('e')
        time.sleep(0.1)  # Adjust the keypress interval if needed
        keyboard.release('e')
        time.sleep(0.1)  # Adjust the key release interval if needed

        # You can adjust the spam_interval to control the pause between spam sessions
        time.sleep(spam_interval)

def main():
    try:
        while True:
            spam_press_key_e(4,0)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
e