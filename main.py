from tkinter import *
from tkinter import messagebox
import pandas

timer = None

BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------ CHANGE CARD AFTER # SEC's ---------------------------------- #
def change_af_3():
    window.after(3000, next_card)


#  ---------------------------- CARD CHANGING MECHANISM  ---------------------------- #
# MECHANISM BRAIN
data = pandas.read_csv('flash-card-project\data\\french_words.csv')
FRENCH_WORDS = [row.French for (index, row) in data.iterrows()]
ENGLISH_WORDS = [row.English for (index, row) in data.iterrows()]
reps = 1
index = 0

# MAIN FUNCTION 1
def next_card():
    global reps
    global index
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    reps += 1
    if reps % 2 == 0:
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(word, text=ENGLISH_WORDS[index % 100],  fill="black")
        canvas.itemconfig(language, text='English',  fill="black")
        print(index, reps)
        timer = window.after(5000, next_card)
    else:
        canvas.itemconfig(card, image=back_card)
        canvas.itemconfig(word, text=FRENCH_WORDS[index % 100], fill="white")
        canvas.itemconfig(language, text="French", fill="white")
        print(index, reps)
        index += 1
        timer = window.after(5000, next_card)

# MAIN FUNCTION 2
def previous_card():
    global reps
    global index
    global timer

    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    
    reps += 1
    if reps % 2 == 0:
        index -= 1
        print(index, reps)
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(word, text=ENGLISH_WORDS[index % 100],  fill="black")
        canvas.itemconfig(language, text='English',  fill="black")
    else:
        print(index, reps)
        canvas.itemconfig(card, image=back_card)
        canvas.itemconfig(word, text=FRENCH_WORDS[index % 100], fill="white")
        canvas.itemconfig(language, text="French", fill="white")


# ----------------------------- UI SETUP ------------------------------------------------ #
window = Tk()
window.title('flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file='flash-card-project\images\card_front.png')
back_card = PhotoImage(file='flash-card-project\images\card_back.png')
card = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="Language", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=('ariel', 60, 'bold'))
canvas.grid(column=1, row=0, columnspan=2)

cross_image = PhotoImage(file='flash-card-project\images\wrong.png')
button_1 = Button(image=cross_image, highlightthickness=0, background=BACKGROUND_COLOR, relief='groove', command=previous_card)
button_1.grid(column=1, row=1)

check_image = PhotoImage(file='flash-card-project\images\\right.png')
button_2 = Button(image=check_image, highlightthickness=0, background=BACKGROUND_COLOR, foreground=BACKGROUND_COLOR, relief='groove', command=next_card)
button_2.grid(column=2, row=1)


window.mainloop()