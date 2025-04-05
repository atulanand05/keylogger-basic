# Keylogger Basic

A simple keylogger script that records keystrokes on your system and stores them locally. It also sends the captured log via email (using Gmail's SMTP server). This is for educational purposes and should be used responsibly.

## Features

- Logs keystrokes in real-time.
- Saves keystroke data into a timestamped log file.


## Installation

1. Clone the repository or download the ZIP file.
2. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `key_logger.py` script.
    ```bash
    python key_logger.py
    ```

2. Press `Esc` to stop the keylogger.
3. The captured log will be saved to your system.
## Configuration

- `log_file`: This variable contains the name of the log file that is being generated. The file name includes a timestamp for uniqueness.

## Contributing

If you'd like to contribute to the development of this project, feel free to fork the repository and submit a pull request.

## Disclaimer

This script is intended for educational purposes only. Misuse of this code could be illegal and unethical. Ensure you have permission before using this script in any environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

