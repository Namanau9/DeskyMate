# 🐱 DeskyMate

A cute animated **desktop pet for Windows** built with Python.
DeskyMate lives on your screen, walks around randomly, reacts to clicks, and occasionally follows your cursor.

It uses **sprite animations and Tkinter** to create a lightweight desktop companion.

---

## 🎬 Demo

![DeskyMate Demo](deskymate_demo.gif)

---

## ✨ Features

* 🐾 Animated idle pet
* 🚶 Random walking around the screen
* 🖱 Occasionally follows your mouse cursor
* 🎭 Random actions (wink, wave, lick, clean)
* 😴 Sleep animation when inactive
* ❤️ Reactions on double-click
* 🖱 Drag pet anywhere on the screen
* 🔍 Adjustable pet size
* 🖥 Transparent background
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

1. Clone the repository

```
git clone https://github.com/yourusername/deskymate.git
cd deskymate
```

2. Install dependencies

```
pip install pillow pynput
```

3. Run the pet

```
python pet.py
```

---

## 📦 Run the Executable

If you downloaded the compiled version:

```
pet.exe
```

Just double-click the file and the pet will appear on your desktop.

---

## 🔧 Adjust Pet Size

You can change the pet size in **pet.py**:

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

The program uses:

* **Tkinter** → transparent always-on-top window
* **Pillow (PIL)** → image loading and scaling
* **pynput** → track mouse and keyboard activity
* **Sprite animation** → idle and sleep states

The pet behavior system includes:

* Idle animation
* Sleep detection
* Random movement
* Cursor tracking
* Interaction reactions

---

## 🚀 Future Improvements

Possible upgrades:

* 🐾 Walking animation while moving
* 🍗 Feeding system
* 💬 Speech bubbles
* 🪑 Sitting on the Windows taskbar
* 🎮 Game detection

---

## 📜 License

MIT License
