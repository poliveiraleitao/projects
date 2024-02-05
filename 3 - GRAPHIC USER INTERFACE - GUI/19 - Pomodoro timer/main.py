import tkinter
from tkinter import Canvas, PhotoImage, Spinbox, StringVar  # Import Canvas and PhotoImage from tkinter module
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2e8b57"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0                                    # work time in minutes
SHORT_BREAK_MIN = 0                             # short break time in minutes
LONG_BREAK_MIN = 20                             # long break time in minutes
REPETITIONS = 0                                 # how many times the timer has started
TOTAL_V = 0                                     # keeps track of the number of V´s to be displayed
CHECKMARK = '✔'
TIMER_IS_ON = None                              # keeps track if you clicked the reset button
ORIGINAL_TOPMOST_STATE = None                   # keep track if the window is on the front screen or not

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPETITIONS

    window.after_cancel(TIMER_IS_ON)                    # this will cancel the timer
    TOTAL_V = 0                                         # reset all variables
    REPETITIONS = 0                                     # reset all variables
    label_pomodoro.config(text="Pomodoro", fg=GREEN)    # reset labels 'Pomodoro'
    canvas.itemconfig(timer_text, text = '00:00')       # reset labels 'timer time'
    check_marks.config(text='')                         # reset labels 'v'
    REPETITIONS = 0                                     # reset repetitions

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global REPETITIONS
    REPETITIONS += 1

    work_sec = WORK_MIN * 60                # calculate the working time in seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # calculate the short break in seconds
    long_break_sec = LONG_BREAK_MIN * 60    # calculate the long break in seconds

    #if it is the 1st/3rd/5th/7th rep:
    if REPETITIONS % 8 == 0:                # if it is the 8th rep:
        count_down(5)
        #count_down(long_break_sec)
        label_pomodoro.config(text="break", fg=RED)
    elif REPETITIONS % 2 == 0:              # if it is the 2nd/4th/6th rep:
        # count_down(short_break_sec)
        count_down(3)
        label_pomodoro.config(text="break", fg=PINK)
    else:                                   # normal work time
        # count_down(work_sec)
        count_down(5)
        label_pomodoro.config(text="Pomodoro", fg=GREEN)    # reset labels 'Pomodoro'
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPETITIONS
    global TOTAL_V
    global TIMER_IS_ON
    global ORIGINAL_TOPMOST_STATE

    # Set topmost state to True before count down
    if count == 0:
        window.wm_attributes("-topmost", True)

    count_min = math.floor(count / 60)         #gets the number of minutes left
    count_sec = count % 60
    if count_sec < 10:                         #avoids displaying 5:0 => 5:00
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # Changes the displayed time in the timer
    if count > 0:
        TIMER_IS_ON = window.after(1000, count_down, count-1) # calls functions count down each 1 second
    else:
        start_timer()
        mark = ''
        if REPETITIONS % 2 == 0:
            TOTAL_V = int(REPETITIONS)/2

        mark += CHECKMARK*int(TOTAL_V)
        check_marks.config(text=mark)

        # Revert topmost state after finishing the timer cycle
        window.wm_attributes("-topmost", ORIGINAL_TOPMOST_STATE)  # To revert

def spinbox_work_time():
    global WORK_MIN
    #gets the current value in spinbox.
    WORK_MIN = int(spinbox_set_work_time.get())

def spinbox_break_time():
    global SHORT_BREAK_MIN
    #gets the current value in spinbox.
    SHORT_BREAK_MIN = int(spinbox_set_break_time.get())

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=20, pady=10, bg=YELLOW)

# spinbox constants
default_work_time = StringVar(value="25")        # Set default work time to 25 minutes
default_break_time = StringVar(value="5")        # Set default break time to 5 minutes
WORK_MIN = int(default_work_time.get())          # preset work_min to 25
SHORT_BREAK_MIN = int(default_break_time.get())  # preset short_break_min to 5

# Spinbox to set work time
spinbox_set_work_time = Spinbox(from_=0, to=30, width=5, textvariable=default_work_time, command=spinbox_work_time)
spinbox_set_work_time.grid(row=0, column=0) #make it apper on the screen
# label Set Work Time
label_work_time = tkinter.Label(text='Work Time', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'))
label_work_time.grid(row=0, column=1, sticky="W") #make it apper on the screen

# Spinbox to set break time
spinbox_set_break_time = Spinbox(from_=0, to=10, width=5, textvariable=default_break_time, command=spinbox_break_time)
spinbox_set_break_time.grid(row=1, column=0) #make it apper on the screen
# label Set Break Time
label_work_time = tkinter.Label(text='Break Time', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'))
label_work_time.grid(row=1, column=1, sticky="W") #make it apper on the screen

# green line
green_line_canvas = Canvas(width=250, height=2, bg=YELLOW, highlightthickness=0)  # Adjust width as needed
green_line_canvas.create_line(0, 1, 1000, 1, fill=GREEN, width=2)
green_line_canvas.grid(row=2, column=1, sticky="N", pady=10)  # Adjust pady as needed

# label Pomodoro Timer
label_pomodoro = tkinter.Label(text='Pomodoro', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'), width=10)
label_pomodoro.grid(row=3, column=1) #make it apper on the screen

# Pomodoro image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img) #start with x and y coord
timer_text = canvas.create_text(107,130, text = '00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=4, column=1)

# Button to start
button = tkinter.Button(text='Start', command=start_timer, font=(FONT_NAME, 12), highlightthickness=0)
button.grid(row=5, column=0, padx=5, pady=5)

# Button to reset
button = tkinter.Button(text='Reset', command=reset_timer, font=(FONT_NAME, 12), highlightthickness=0)
button.grid(row=5, column=2, padx=5, pady=5)

#checkmarks
check_marks = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_marks.grid(row=5, column=1, padx=5, pady=20)

ORIGINAL_TOPMOST_STATE = window.wm_attributes("-topmost")  # Get initial topmost state

window.mainloop()