import tkinter as tk
import random

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Rock Paper Scissors - Next Level")
root.geometry("620x700")
root.config(bg="#0f172a")

# ---------------- VARIABLES ----------------

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0
round_count = 0

# ---------------- FUNCTIONS ----------------

def animate_thinking(user_choice):
    result_label.config(text="Computer is thinking...", fg="#facc15")
    root.after(700, lambda: play(user_choice))

def play(user_choice):
    global user_score, computer_score, round_count

    computer_choice = random.choice(choices)
    round_count += 1

    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie 🤝"
        color = "#facc15"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win 🎉"
        color = "#22c55e"
        user_score += 1

    else:
        result = "Computer Wins 🤖"
        color = "#ef4444"
        computer_score += 1

    result_label.config(text=result, fg=color)

    score_label.config(
        text=f"Score | You: {user_score}   Computer: {computer_score}"
    )

    round_label.config(text=f"Round: {round_count}")

def reset_game():
    global user_score, computer_score, round_count

    user_score = 0
    computer_score = 0
    round_count = 0

    score_label.config(text="Score | You: 0   Computer: 0")
    round_label.config(text="Round: 0")

    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="Game Reset! Choose again", fg="white")

# ---------------- HOVER EFFECT ----------------

def on_enter(e):
    e.widget['bg'] = "#38bdf8"

def on_leave(e):
    e.widget['bg'] = "#1e293b"

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Helvetica", 30, "bold"),
    fg="white",
    bg="#0f172a"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Next Level Premium Edition",
    font=("Arial", 13),
    fg="#94a3b8",
    bg="#0f172a"
)

subtitle.pack()

# ---------------- SCORE ----------------

score_label = tk.Label(
    root,
    text="Score | You: 0   Computer: 0",
    font=("Arial", 15, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)

score_label.pack(pady=10)

round_label = tk.Label(
    root,
    text="Round: 0",
    font=("Arial", 12),
    fg="#cbd5f5",
    bg="#0f172a"
)

round_label.pack()

# ---------------- BUTTON AREA ----------------

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=40)

btn_style = {
    "font": ("Arial", 16, "bold"),
    "width": 12,
    "height": 2,
    "bg": "#1e293b",
    "fg": "white",
    "bd": 0
}

rock = tk.Button(frame, text="🪨 Rock", command=lambda: animate_thinking("Rock"), **btn_style)
paper = tk.Button(frame, text="📄 Paper", command=lambda: animate_thinking("Paper"), **btn_style)
scissors = tk.Button(frame, text="✂ Scissors", command=lambda: animate_thinking("Scissors"), **btn_style)

rock.grid(row=0, column=0, padx=15)
paper.grid(row=0, column=1, padx=15)
scissors.grid(row=0, column=2, padx=15)

for btn in [rock, paper, scissors]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ---------------- RESULT AREA ----------------

user_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    fg="white",
    bg="#0f172a"
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    fg="white",
    bg="#0f172a"
)
computer_choice_label.pack()

result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 20, "bold"),
    fg="#22c55e",
    bg="#0f172a"
)
result_label.pack(pady=30)

# ---------------- RESET BUTTON ----------------

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 13, "bold"),
    bg="#ef4444",
    fg="white",
    width=15,
    height=2,
    bd=0,
    command=reset_game
)

reset_btn.pack(pady=20)

# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="Developer: Roshni Tirkey",
    font=("Arial", 11),
    fg="#64748b",
    bg="#0f172a"
)

footer.pack(side="bottom", pady=10)

# ---------------- RUN ----------------

root.mainloop()