# Keylogging Task
Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.

## Keylogger Tool

This repository contains a simple keylogger tool that logs keystrokes to a text file using the `pynput` library.

### Features

- Logs all keystrokes, including special keys.
- Saves the logged keystrokes to a specified text file (`keylog.txt`).

### Dependencies

- `pynput` library

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/keylogger-tool.git
    cd keylogger-tool
    ```

2. **Install the required dependencies**:
    ```bash
    pip install pynput
    ```

### Usage

1. **Run the script**:
    ```bash
    python task4.py
    ```

2. **Logging keystrokes**:
    - The keystrokes will be logged to `keylog.txt` in the current directory.
    - To stop the keylogger, press the `esc` key.

### Example

Running the script:
```bash
python keylogger_tool.py
```

Output in `keylog.txt`:
```
h e l l o [Key.space] w o r l d [Key.enter] [Key.esc]
```

### Functions

- **on_press(key)**:
  - Logs the pressed key to `keylog.txt`.
  - Parameters:
    - `key`: The key that was pressed.
  - Handles both character keys and special keys.

- **on_release(key)**:
  - Handles key release events.
  - Parameters:
    - `key`: The key that was released.
  - Stops the keylogger when the `esc` key is pressed.

### Disclaimer

This tool is intended for educational purposes only. Use it responsibly and ensure you have permission to log keystrokes on any system.
