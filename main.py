import math
from  tkinter import  *
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer= 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN ,bg=YELLOW, font=(FONT_NAME , 55 , "bold" ))
    check_label.config(text = "")
    global reps
    reps =0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    reps += 1

    if reps%2!=0:
        count_down(25*60)
        timer_label.config(text="Work", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))


    elif  reps%2==0:
        count_down(5*60)
        timer_label.config(text="Break",foreground=PINK ,bg=YELLOW, font=(FONT_NAME , 55 , "bold" ) )


    elif reps%8==0:
        count_down(20*60)
        timer_label.config(text="Break", foreground=RED, bg=YELLOW, font=(FONT_NAME, 55, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minute = math.floor(count/60)
    count_seconds = count%60
    canvas.itemconfig(timer_text , text=f"{count_minute}:{count_seconds}")
    if count>0:
        global timer
        timer = window.after(1000 ,count_down , count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            marks = "✓"
            check_label.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100 , pady=100,  bg=YELLOW)

canvas = Canvas(width =200 , height=224 , bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103 , 112 , image=tomato_image)
timer_text= canvas.create_text(100 , 130 , text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold" ))
canvas.grid(column=1 , row=1)


timer_label =tkinter.Label(text="Timer", foreground=GREEN ,bg=YELLOW, font=(FONT_NAME , 55 , "bold" ))
timer_label.grid(column=1 , row=0)

start_button= tkinter.Button(text="Start" , command=start_timer)
start_button.grid(column=0 , row=2)

reset_button= tkinter.Button(text="Reset" , command=reset_timer)
reset_button.grid(column=2 , row=2)

check_label= tkinter.Label(text="" , foreground=GREEN , bg=YELLOW)
check_label.grid(column=1 , row=3)









window.mainloop()




























































































