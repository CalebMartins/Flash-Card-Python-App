    print(index_2)
            canvas.itemconfig(card, image=back_card)
            canvas.itemconfig(word, text=FRENCH_WORDS[(index_2 - 1) % 100], fill="white")
            canvas.itemconfig(language, text="French", fill="white")
