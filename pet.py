import tkinter as tk
from PIL import Image, ImageTk
import itertools
import random
import time
import sys
import os
from pynput import mouse, keyboard

# ----------------------------
# SETTINGS
# ----------------------------

SCALE = 0.45   # change pet size here

# ----------------------------
# RESOURCE PATH (FOR EXE)
# ----------------------------

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ----------------------------
# USER ACTIVITY
# ----------------------------

last_activity = time.time()
cursor_x = 0
cursor_y = 0

def update_activity():
    global last_activity
    last_activity = time.time()

def on_press(key):
    update_activity()

def on_move(x, y):
    global cursor_x, cursor_y
    cursor_x = x
    cursor_y = y
    update_activity()

def on_click(x, y, button, pressed):
    update_activity()

keyboard.Listener(on_press=on_press).start()
mouse.Listener(on_move=on_move, on_click=on_click).start()

# ----------------------------
# WINDOW
# ----------------------------

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)

root.config(bg="black")
root.attributes("-transparentcolor", "black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack()

# ----------------------------
# IMAGE LOADER
# ----------------------------

def load(name, flip=False):

    path = resource_path(f"assets/{name}.png")

    img = Image.open(path)

    new_w = int(img.width * SCALE)
    new_h = int(img.height * SCALE)

    img = img.resize((new_w, new_h), Image.NEAREST)

    if flip:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    return ImageTk.PhotoImage(img)

# ----------------------------
# SPRITES
# ----------------------------

idle_right = [
    load("idle1"),
    load("idle2"),
    load("idle3"),
    load("idle4")
]

idle_left = [
    load("idle1", True),
    load("idle2", True),
    load("idle3", True),
    load("idle4", True)
]

sleep_frames = [
    load("sleep1"),
    load("sleep2")
]

sprites = {
    "eat": load("eat"),
    "hungry": load("hungry"),
    "excited": load("excited"),
    "love": load("love"),
    "wave": load("wave"),
    "wink": load("wink"),
    "lick": load("lick"),
    "clean": load("clean")
}

idle_cycle_right = itertools.cycle(idle_right)
idle_cycle_left = itertools.cycle(idle_left)
sleep_cycle = itertools.cycle(sleep_frames)

pet_w = idle_right[0].width()
pet_h = idle_right[0].height()

canvas.config(width=pet_w, height=pet_h)

# ----------------------------
# SCREEN SIZE
# ----------------------------

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ----------------------------
# PET POSITION
# ----------------------------

x = random.randint(0, screen_width - pet_w)
y = screen_height - pet_h - 40

pet = canvas.create_image(pet_w//2, pet_h//2, image=idle_right[0])

state = "idle"
direction = 1

# ----------------------------
# ANIMATION
# ----------------------------

def animate():

    global state

    idle_time = time.time() - last_activity

    if idle_time > 20:
        state = "sleep"

    if state == "idle":

        if direction == 1:
            frame = next(idle_cycle_right)
        else:
            frame = next(idle_cycle_left)

        canvas.itemconfig(pet, image=frame)

    elif state == "sleep":

        frame = next(sleep_cycle)
        canvas.itemconfig(pet, image=frame)

    root.after(300, animate)

# ----------------------------
# RANDOM WALK
# ----------------------------

def walk_random():

    global x, direction

    if state != "sleep":

        direction = random.choice([-1, 1])

        distance = random.randint(120, 300)
        steps = distance // 10

        def move(step=0):

            global x

            if step < steps:

                x += direction * 10

                if x < 0:
                    x = 0

                if x > screen_width - pet_w:
                    x = screen_width - pet_w

                root.geometry(f"+{x}+{y}")

                root.after(50, lambda: move(step + 1))

        move()

    root.after(random.randint(9000, 15000), walk_random)

# ----------------------------
# FOLLOW CURSOR SOMETIMES
# ----------------------------

def follow_cursor():

    global x, direction

    if random.random() < 0.35:

        target = cursor_x

        direction = 1 if target > x else -1

        steps = 40

        def move(step=0):

            global x

            if step < steps:

                if x < target:
                    x += 8
                else:
                    x -= 8

                if x < 0:
                    x = 0

                if x > screen_width - pet_w:
                    x = screen_width - pet_w

                root.geometry(f"+{x}+{y}")

                root.after(40, lambda: move(step + 1))

        move()

    root.after(random.randint(15000, 22000), follow_cursor)

# ----------------------------
# RANDOM ACTIONS
# ----------------------------

def random_action():

    if state == "idle":

        action = random.choice([
            "wink",
            "wave",
            "lick",
            "clean"
        ])

        canvas.itemconfig(pet, image=sprites[action])

        root.after(2000, set_idle)

    root.after(10000, random_action)

def set_idle():
    global state
    state = "idle"

# ----------------------------
# CLICK REACTION
# ----------------------------

def pet_clicked(event):

    reaction = random.choice([
        "love",
        "excited",
        "eat"
    ])

    canvas.itemconfig(pet, image=sprites[reaction])

    root.after(2000, set_idle)

canvas.bind("<Double-Button-1>", pet_clicked)

# ----------------------------
# DRAG PET
# ----------------------------

def drag_start(event):
    root.x = event.x
    root.y = event.y

def drag_motion(event):

    global x, y

    x = event.x_root - root.x
    y = event.y_root - root.y

    root.geometry(f"+{x}+{y}")

canvas.bind("<Button-1>", drag_start)
canvas.bind("<B1-Motion>", drag_motion)

# ----------------------------
# CLOSE OPTION
# ----------------------------

root.bind("<Escape>", lambda e: root.destroy())

# ----------------------------
# START
# ----------------------------

root.geometry(f"{pet_w}x{pet_h}+{x}+{y}")

animate()
walk_random()
random_action()
follow_cursor()

try:
    root.mainloop()
except KeyboardInterrupt:
    root.destroy()