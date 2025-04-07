# 🔐 Silent Keylogger with Timestamp Logging (Educational Use Only)

This is a **stealth keylogger** written in Python using the `pynput` library. It logs all keyboard input (including special keys) to a timestamped `.txt` file — completely silently, with **no console messages or alerts**.

> ⚠️ **Warning — Use Responsibly**  
> This software is provided strictly for **educational and ethical purposes** only.  
> Unauthorized use to monitor others without consent is illegal and unethical.  
> Always obtain **explicit permission** before running this script on any machine you do not personally own.

---

## 🧩 Features

- ✅ Logs **all keypresses**, including letters, numbers, symbols, and special keys  
- ✅ Adds a **timestamp** to every key press  
- ✅ Creates a **new log file** for every session (e.g., `keylog_20250407_161042.txt`)  
- ✅ Operates in **stealth mode** – no window, messages, or alerts  
- ✅ Automatically stops when **`Esc` key is pressed**  

---

## 🔧 Requirements

- Python 3.6 or higher  
- `pynput` module  

Install `pynput` with:

```bash
pip install pynput
```
## 🚀 How to Use

Follow these steps to download, run, and stop the keylogger script:

---

### ✅ 1. Download or Clone the Repository

You have two options:

#### 🔹 Option A: Download as ZIP (No Git Required)

1. Go to [https://github.com/atulanand05/keylogger](https://github.com/atulanand05/keylogger)
2. Click the green **"Code"** button and select **"Download ZIP"**.
3. Extract the downloaded ZIP file.
4. Open a terminal and navigate into the extracted folder using:

   ```bash
   cd path/to/extracted/keylogger-folder
Example (if extracted in Downloads):
    ```bash
    cd Downloads/keylogger-main

🔹 Option B: Clone with Git (Recommended)
Open a terminal and run:

    git clone https://github.com/atulanand05/keylogger.git
    cd keylogger

✅ 2. Make Sure Python is Installed
To check if Python is installed, run:

    python --version

or

    python3 --version

If not installed, download it from: https://www.python.org/downloads

    ✅ Make sure to select “Add Python to PATH” during installation.

✅ 3. Install Required Packages
The script uses the pynput library. To install it, run:

    pip install pynput

If needed, try:

    pip install --user pynput

✅ 4. Run the Script
In the terminal, make sure you're inside the keylogger folder, then run:

    python keylogger.py
Or, if using python3:

python3 keylogger.py

The keylogger will now start running in the background and begin logging keystrokes.

🛑 5. Stop the Keylogger
To stop it, simply press the Esc key on your keyboard.

## 📁 Output

Each session creates a new log file in the current directory:

```
keylog_YYYYMMDD_HHMMSS.txt
```

Example contents:

```
[16:10:42] a
[16:10:43] b
[16:10:44] [Key.space]
[16:10:45] [Key.enter]
```

---

## ⚖️ Legal & Ethical Disclaimer

This script is for:

- ✅ Learning how low-level keyboard monitoring works  
- ✅ Building input tracking tools for accessibility or automation  
- ✅ Security research on keylogging behavior  

**It must not be used to:**

- ❌ Spy on users without knowledge  
- ❌ Record passwords or personal info  
- ❌ Break laws or violate privacy  

> By using this software, you agree to use it only in a legal and ethical manner.  
> The author is **not responsible** for misuse or any resulting consequences.

---

## 🪪 License

This project is licensed under the **MIT License**. You are free to use, modify, and share it **for ethical purposes only**.
See the full [LICENSE](LICENSE).