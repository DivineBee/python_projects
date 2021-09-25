from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomo():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_pomo():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK", fg=RED)
        countdown(long_break)
    elif reps % 2 == 0:
        title_label.config(text="SHORT BREAK", fg=PINK)
        countdown(short_break)
    else:
        title_label.config(text="WORK", fg=GREEN)
        countdown(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_pomo()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"

        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 30, "bold"), fg=GREEN)
title_label.grid(column=1, row=0)

start_btn = Button(text="START", command=start_pomo, fg="white", bg=GREEN, font=(FONT_NAME, 16, "bold"))
start_btn.grid(column=0, row=2)
reset_btn = Button(text="RESET", command=reset_pomo, fg="white", bg=PINK, font=(FONT_NAME, 16, "bold"))
reset_btn.grid(column=2, row=2)

check_label = Label(bg=YELLOW, font=(FONT_NAME, 20, "bold"), fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
