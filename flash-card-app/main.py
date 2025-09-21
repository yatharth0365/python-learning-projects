from tkinter import*
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/words_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title,text = "French",fill ="black")
    canvas.itemconfig(card_word,text = current_card["French"],fill ="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"],fill = "white")
    canvas.itemconfig(card_background, image= card_back)

def is_known():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400 , 150, text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400 , 263, text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown = Button(image=cross_image,command=next_card)
unknown.grid(row=1,column=0)
unknown.config(bg=BACKGROUND_COLOR,highlightthickness=0)

check_image = PhotoImage(file="images/right.png")
known = Button(image=check_image,command=is_known)
known.grid(row=1,column=1)
known.config(bg=BACKGROUND_COLOR,highlightthickness=0)

next_card()













window.mainloop()