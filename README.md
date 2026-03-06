# 🐱 DeskyMate

A cute animated **desktop pet for Windows** built with Python.

DeskyMate lives on your desktop, walks around randomly, reacts to clicks, performs idle animations, and sometimes follows your mouse cursor.

The project uses **sprite animation + Tkinter** to create a lightweight desktop companion.

---

## 🎬 Demo
![deskymate_demo](https://github.com/user-attachments/assets/b0a83ed2-fede-4ef6-a2a0-692a53ab1c0e)



---

## ✨ Features

* 🐾 Animated idle pet
* 🚶 Random walking across the screen
* 🖱 Occasionally follows the mouse cursor
* 🎭 Random behaviors (wink, wave, lick, clean)
* 😴 Sleep animation when the computer is inactive
* ❤️ Reactions on double-click
* 🖱 Drag the pet anywhere on the screen
* 🔍 Adjustable pet size
* 🖥 Transparent background window
* 📦 Can be compiled into a standalone `.exe`

---

## 🎮 Controls

| Action           | Result     |
| ---------------- | ---------- |
| Double-click pet | Pet reacts |
| Drag pet         | Move pet   |
| ESC              | Close pet  |

---

## 📂 Project Structure

```
DeskyMate
│
├── pet.py
├── icon.ico
├── assets
│   ├ idle1.png
│   ├ idle2.png
│   ├ idle3.png
│   ├ idle4.png
│   ├ sleep1.png
│   ├ sleep2.png
│   ├ eat.png
│   ├ hungry.png
│   ├ excited.png
│   ├ love.png
│   ├ wave.png
│   ├ wink.png
│   ├ lick.png
│   └ clean.png
```

---

## ⚙️ Installation (Run from Python)

Clone the repository:

```
git clone https://github.com/Namanau9/DeskyMate.git
cd DeskyMate
```

Install dependencies:

```
pip install pillow pynput
```

Run the program:

```
python pet.py
```

---

## 📦 Running the Executable

If you download the compiled version:

```
pet.exe
```

Just double-click the file and the pet will appear on your desktop.

---

## 🔧 Adjust Pet Size

You can modify the pet size inside **pet.py**:

```
SCALE = 0.45
```

Example values:

| Value | Size   |
| ----- | ------ |
| 0.35  | Small  |
| 0.45  | Medium |
| 0.60  | Large  |

---

## 🧠 How It Works

The project uses:

* **Tkinter** → transparent always-on-top window
* **Pillow (PIL)** → image loading and scaling
* **pynput** → track mouse and keyboard activity
* **Sprite animations** → idle and sleep states

The pet behavior system includes:

* Idle animation
* Sleep detection
* Random movement
* Cursor tracking
* Interaction reactions

---

## 🚀 Future Improvements

Planned features:

* 🐾 Real walking animation
* 🍗 Feeding system
* 💬 Speech bubbles
* 🪑 Sitting on the Windows taskbar
* 🎮 Game detection

---

## 📜 License

MIT License
