import math
import tkinter as tk
from tkinter import font as tkfont


COLORS = {
    "bg_top": "#0b1020",
    "bg_bottom": "#05060d",
    "card": "#0f172a",
    "card_border": "#1e293b",
    "text_primary": "#f8fafc",
    "text_muted": "#94a3b8",
    "accent": "#22d3ee",
    "accent_2": "#a855f7",
    "entry_bg": "#0b1220",
    "entry_border": "#1f2937",
    "button_bg": "#22d3ee",
    "button_fg": "#001018",
    "button_active": "#06b6d4",
}

MAX_DISPLAY = 200


def fib_sequence(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def fib_stats(n):
    a, b = 0, 1
    total = 0
    last = 0
    for _ in range(n):
        total += a
        last = a
        a, b = b, a + b
    return last, total


def hex_blend(c1, c2, t):
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def round_rect(canvas, x1, y1, x2, y2, radius=20, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


root = tk.Tk()
root.title("Fibonacci Atelier")
root.geometry("980x580")
root.minsize(900, 520)
root.configure(bg=COLORS["bg_bottom"])
root.tk.call("tk", "scaling", 1.15)

title_font = tkfont.Font(family="Segoe UI", size=28, weight="bold")
subtitle_font = tkfont.Font(family="Segoe UI", size=12)
label_font = tkfont.Font(family="Segoe UI", size=11, weight="bold")
stat_value_font = tkfont.Font(family="Segoe UI", size=16, weight="bold")
stat_label_font = tkfont.Font(family="Segoe UI", size=9)

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

card_frame = tk.Frame(canvas, bg=COLORS["card"], padx=28, pady=24)

header = tk.Frame(card_frame, bg=COLORS["card"])
header.grid(row=0, column=0, sticky="ew", pady=(6, 18))
header.columnconfigure(0, weight=1)

title = tk.Label(
    header,
    text="Fibonacci Atelier",
    fg=COLORS["text_primary"],
    bg=COLORS["card"],
    font=title_font,
)
title.grid(row=0, column=0, sticky="w")

subtitle = tk.Label(
    header,
    text="A luminous sequence generator",
    fg=COLORS["text_muted"],
    bg=COLORS["card"],
    font=subtitle_font,
)
subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

input_row = tk.Frame(card_frame, bg=COLORS["card"])
input_row.grid(row=1, column=0, sticky="ew", pady=(0, 18))
input_row.columnconfigure(1, weight=1)

tk.Label(
    input_row,
    text="COUNT",
    fg=COLORS["text_muted"],
    bg=COLORS["card"],
    font=label_font,
).grid(row=0, column=0, sticky="w", padx=(0, 12))

entry_border = tk.Frame(
    input_row,
    bg=COLORS["entry_border"],
    padx=1,
    pady=1,
)
entry_border.grid(row=0, column=1, sticky="ew")

entry = tk.Entry(
    entry_border,
    bg=COLORS["entry_bg"],
    fg=COLORS["text_primary"],
    insertbackground=COLORS["accent"],
    relief="flat",
    highlightthickness=0,
    font=subtitle_font,
)
entry.pack(fill="x", ipady=6)
entry.insert(0, "20")

generate_btn = tk.Button(
    input_row,
    text="Generate",
    bg=COLORS["button_bg"],
    fg=COLORS["button_fg"],
    activebackground=COLORS["button_active"],
    activeforeground=COLORS["button_fg"],
    relief="flat",
    padx=18,
    pady=6,
    cursor="hand2",
    font=label_font,
)
generate_btn.grid(row=0, column=2, padx=(12, 0))

stats_row = tk.Frame(card_frame, bg=COLORS["card"])
stats_row.grid(row=2, column=0, sticky="ew", pady=(0, 18))
for i in range(3):
    stats_row.columnconfigure(i, weight=1)


def stat_block(parent, label_text):
    frame = tk.Frame(parent, bg=COLORS["entry_bg"], bd=1, relief="flat")
    label = tk.Label(
        frame,
        text=label_text,
        fg=COLORS["text_muted"],
        bg=COLORS["entry_bg"],
        font=stat_label_font,
    )
    value = tk.Label(
        frame,
        text="0",
        fg=COLORS["text_primary"],
        bg=COLORS["entry_bg"],
        font=stat_value_font,
    )
    label.pack(anchor="w", padx=10, pady=(8, 0))
    value.pack(anchor="w", padx=10, pady=(0, 10))
    return frame, value


count_block, count_value = stat_block(stats_row, "COUNT")
count_block.grid(row=0, column=0, sticky="ew", padx=(0, 10))

last_block, last_value = stat_block(stats_row, "LAST VALUE")
last_block.grid(row=0, column=1, sticky="ew", padx=10)

sum_block, sum_value = stat_block(stats_row, "SUM")
sum_block.grid(row=0, column=2, sticky="ew", padx=(10, 0))

output_label = tk.Label(
    card_frame,
    text="SEQUENCE OUTPUT",
    fg=COLORS["text_muted"],
    bg=COLORS["card"],
    font=label_font,
)
output_label.grid(row=3, column=0, sticky="w")

output_border = tk.Frame(card_frame, bg=COLORS["entry_border"], padx=1, pady=1)
output_border.grid(row=4, column=0, sticky="nsew", pady=(8, 0))

output = tk.Text(
    output_border,
    height=6,
    bg=COLORS["entry_bg"],
    fg=COLORS["text_primary"],
    insertbackground=COLORS["accent"],
    highlightthickness=0,
    relief="flat",
    wrap="word",
    font=subtitle_font,
)
output.pack(fill="both", expand=True, padx=4, pady=4)
output.configure(state="disabled")

helper = tk.Label(
    card_frame,
    text=f"Hint: values are capped for display at {MAX_DISPLAY}.",
    fg=COLORS["text_muted"],
    bg=COLORS["card"],
    font=stat_label_font,
)
helper.grid(row=5, column=0, sticky="w", pady=(10, 0))

card_frame.columnconfigure(0, weight=1)
card_frame.rowconfigure(4, weight=1)

state = {"card_window": None, "glow_id": None, "phase": 0.0}


def set_output(text):
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.insert("1.0", text)
    output.configure(state="disabled")


def on_generate(event=None):
    value = entry.get().strip()
    try:
        n = int(value)
    except ValueError:
        set_output("Please enter a whole number.")
        return

    if n < 0:
        set_output("Please enter a non-negative number.")
        return

    last, total = fib_stats(n)
    count_value.config(text=str(n))
    last_value.config(text=str(last))
    sum_value.config(text=str(total))

    display_n = min(n, MAX_DISPLAY)
    seq = fib_sequence(display_n)
    text = " ".join(str(x) for x in seq)
    if n > MAX_DISPLAY:
        text = f"{text} ... (showing first {MAX_DISPLAY})"
    set_output(text)


def draw_background(event=None):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    if width <= 0 or height <= 0:
        return

    canvas.delete("bg")
    canvas.delete("card_shape")
    canvas.delete("glow")
    state["glow_id"] = None

    for i in range(height):
        t = i / max(height - 1, 1)
        color = hex_blend(COLORS["bg_top"], COLORS["bg_bottom"], t)
        canvas.create_line(0, i, width, i, fill=color, tags="bg")

    accents = [
        (0.12, 0.22, 240, COLORS["accent"]),
        (0.82, 0.18, 180, COLORS["accent_2"]),
        (0.9, 0.72, 260, "#38bdf8"),
    ]
    for x_ratio, y_ratio, size, color in accents:
        x = width * x_ratio
        y = height * y_ratio
        canvas.create_oval(
            x - size, y - size, x + size, y + size,
            fill=color,
            outline="",
            tags="bg",
        )

    stars = [
        (0.18, 0.12, 3),
        (0.28, 0.32, 2),
        (0.48, 0.18, 2),
        (0.72, 0.3, 3),
        (0.85, 0.58, 2),
        (0.65, 0.78, 2),
    ]
    for x_ratio, y_ratio, size in stars:
        x = width * x_ratio
        y = height * y_ratio
        canvas.create_oval(
            x - size, y - size, x + size, y + size,
            fill="#e2e8f0",
            outline="",
            tags="bg",
        )

    card_width = min(720, width - 80)
    card_height = min(400, height - 140)
    card_x1 = (width - card_width) / 2
    card_y1 = (height - card_height) / 2
    card_x2 = card_x1 + card_width
    card_y2 = card_y1 + card_height

    round_rect(
        canvas,
        card_x1,
        card_y1,
        card_x2,
        card_y2,
        radius=24,
        fill=COLORS["card"],
        outline=COLORS["card_border"],
        width=2,
        tags="card_shape",
    )

    if state["card_window"] is None:
        state["card_window"] = canvas.create_window(
            (width / 2, height / 2),
            window=card_frame,
            anchor="center",
            tags="card_window",
            width=card_width - 40,
        )
    else:
        canvas.coords(state["card_window"], width / 2, height / 2)
        canvas.itemconfigure(state["card_window"], width=card_width - 40)

    glow_x = card_x2 - 80
    glow_y = card_y1 + 60
    if state["glow_id"] is None:
        state["glow_id"] = canvas.create_oval(
            glow_x - 40,
            glow_y - 40,
            glow_x + 40,
            glow_y + 40,
            fill=COLORS["accent"],
            outline="",
            tags="glow",
        )
    else:
        canvas.coords(
            state["glow_id"],
            glow_x - 40,
            glow_y - 40,
            glow_x + 40,
            glow_y + 40,
        )


def pulse():
    state["phase"] += 0.05
    glow = (math.sin(state["phase"]) + 1) / 2
    color = hex_blend(COLORS["accent"], COLORS["accent_2"], glow)
    if state["glow_id"] is not None:
        canvas.itemconfigure(state["glow_id"], fill=color)
    root.after(60, pulse)


generate_btn.config(command=on_generate)
entry.bind("<Return>", on_generate)

canvas.bind("<Configure>", draw_background)

entry.focus()
on_generate()
draw_background()
pulse()

root.mainloop()
