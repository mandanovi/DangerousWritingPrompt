from tkinter import *


class DangerousWriting(Tk):
    def __init__(self):
        super().__init__()
        self.title("DANGEROUS WRITING PROMPT")
        self.geometry("1200x450")  # Define the geometry of the window
        self.configure(bg='white')
        self.widget()
        self.count = 0
        self.user_write = False

    def widget(self):
        title = Label(width=48, text="Dangerous Writing Prompt", font=("Arial Black", 25), fg='#251B37', bg='white')
        title.grid(column=1, row=1, columnspan=5, sticky=W+E, padx=50)
        rule = Label(width=100, text="Write anything and do not stop, 5 seconds no activities, all text will disappear.",
                     font=("Arial Black", 11),
                     fg='#FFCACA', bg='#251B37')
        rule.grid(column=1, row=2, columnspan=5, sticky=W+E)
        self.sentence = Text(self, height=8, width=130, highlightthickness=1, font=("Arial Black", 10))
        self.sentence.grid(column=1, row=3, columnspan=5, pady=50)
        self.sentence.bind("<Key>", self.user_typing)

    def count_down(self):
        if self.user_write:
            self.count +=1
            self.count_label = Label(width=50, text=f"{self.count}", font=("Arial Black", 10), fg='#251B37', bg='white')
            self.count_label.grid(column=2, row=5, columnspan=5, sticky=W+E)
            if self.count > 5:
                self.counting_words()
                self.sentence.delete("1.0", END)
                self.user_write = False
                self.reset()
            self.after(1000, self.count_down)

    def counting_words(self):
        sentence = self.sentence.get("1.0", "end-1c")
        total_words = str(len(sentence.split()))
        self.count_label.config(text=f"You lose your text. You have written {total_words} words.")

    def user_typing(self, event):
        if self.user_write:
            self.reset()
        else:
            self.user_write = True
            self.count_down()

    def reset(self):
        self.count = 0


App = DangerousWriting()
App.mainloop()
