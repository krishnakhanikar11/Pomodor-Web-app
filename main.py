from tkinter import *
import math

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



window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 100, bg = YELLOW )

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text= "Timer")
    global reps
    reps = 0

def start_timer():
    global reps
    reps = reps+1
    wor_sec= WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps %8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)

    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)

    else:
        count_down(wor_sec)
        title_label.config(text="WORK", fg=GREEN)



def count_down(count):
    con_min = math.floor(count/60)
    con_sec= count%60

    if  con_sec<10:
        con_sec = f'0{con_sec}'

    canvas.itemconfig(timer_text,text=f"{con_min}:{con_sec}")

    if count>0:
        global timer
        timer = window.after(1000,count_down, count-1)

    else:
        start_timer()
        global reps
        rep_list = ""
        work_session = math.floor(reps%2)
        for _ in range(0,work_session):
            rep_list = rep_list + "✔"
        title_label1.config(text=rep_list)
        

title_label = Label(text="Timer", fg= GREEN,font= (FONT_NAME, 50) ,bg=YELLOW)
title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row = 0, column = 1)


canvas = Canvas(width = 200, height= 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


start_button = Button(text="Start", command=start_timer, highlightthickness = 0)
start_button.grid(row = 2, column = 0)

title_label1 = Label( bg= YELLOW,fg= GREEN)
title_label1.grid(row = 2, column = 1)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness = 0)
reset_button.grid(row = 2, column = 2)


window.mainloop()