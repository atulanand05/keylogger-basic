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

---

## 🚀 How to Use

1. **Download or clone** this repository:

```bash
git clone https://github.com/atulanand05/keylogger.git
cd keylogger
```

2. **Run the script** (it will immediately start logging):

```bash
python keylogger.py
```

3. **To stop logging**, simply press the `Esc` key.

---

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