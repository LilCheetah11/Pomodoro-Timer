
from email.mime import image

from tkinter import *
from cgitb import text
import math
# ---------------------------- CONSTANTS ------------------------------- #



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps=0
timer= NONE


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")

    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec=(WORK_MIN*60)
    short_break_sec=(SHORT_BREAK_MIN*60)
    long_break_sec= (LONG_BREAK_MIN*60)


    if reps%2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=PINK)

    elif reps%8 ==0 :
        count_down(long_break_sec)
        timer_label.config(text="Break",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=RED)

    else:
        count_down(work_sec)
        
        timer_label.config(text="Work",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=GREEN)    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min=math.floor(count/60)
    count_seconds=count%60
    # count_sec=str(count_seconds)
    # if len(count_sec)<2:
    if count_seconds<10:
        count_seconds=f"0{count_seconds}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_seconds}")
    if count >0:
        global timer
        timer=window.after(1000,count_down, count -1)

    else:
        start_timer()
        
        mark=""
        num_check=math.floor(reps/2)
        for _ in range(num_check):
            mark += "✔"
        checkmark_label.config(text=mark,font=(FONT_NAME,15,"bold"),bg=YELLOW,fg=GREEN)    
    
# ---------------------------- UI SETUP ------------------------------- #


#Creating a new window and configurations
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100,pady=100,background=YELLOW)



canvas=Canvas(width=220,height=300,background=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110,150,image=tomato_img)
timer_text=canvas.create_text(110,175,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

#Labels
timer_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=GREEN)

timer_label.grid(column=2,row=1)



#Labels
checkmark_label = Label(text="",font=(FONT_NAME,15,"bold"),bg=YELLOW,fg=GREEN)

checkmark_label.grid(column=2,row=3)



#Buttons


#calls action() when pressed
start_button = Button(text="Start", command=start_timer ,font=(FONT_NAME,10,"bold"))
start_button.grid(column=1,row=3)


#Buttons
# def action():
#     print("Do something")

#calls action() when pressed
button = Button(text="Reset", command=reset_timer,font=(FONT_NAME,10,"bold"))
button.grid(column=3,row=3)





window.mainloop()