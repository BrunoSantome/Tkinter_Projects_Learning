import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Style
import random
import ctypes


class Aplication(tk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Typing Speed Test")
        main_window.configure(width=800, height=800)

    def initiate_senteces(self):
        sentences = [
            "Bilbo was very rich and very peculiar, and had been the wonderof the Shire for sixty years, ever since his remarkable disappearance and unexpected return. The riches he had brought back from his travels had now become a local legend, and it was popularly believed, whatever the old folk might say, that the Hill at Bag End was full of tunnels stuffed with treasure. And if that was not enough for fame, there was also his prolonged vigour to marvel a",
            "The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a batteries include language due to its comprehensive standard library."
        ]
        return random.choice(sentences).lower()

    def draw(self):
        self.mainframe = ttk.Frame(main_window)
        self.mainframe.pack(anchor=tk.CENTER)
        self.style = Style()
        self.style.configure('W.TButton', font=(
            'calibri', 10, 'bold', 'underline'))
        self.style.configure('W.TButton', font=(
            'calibri', 10, 'bold', 'underline'))
        self.titlelabel = ttk.Label(
            self.mainframe, text="Typing Speed Test", font=('castellar', 30))
        self.startbtn = ttk.Button(
            self.mainframe, text="Start Test", style='W.TButton', width=20, command=self.test_window)
        self.titlelabel.pack(anchor=tk.CENTER, pady=30)
        self.startbtn.pack(anchor=tk.CENTER, pady=20)

    def test_window(self):
        self.splitpoint = 0
        self.passedSeconds = 0
        self.String = ""
        self.sentence = self.initiate_senteces()
        self.TestOn = True
        self.window2 = tk.Toplevel(main_window)
        self.window2.title("Test")

        self.WrittenText = tk.Label(
            self.window2, text=self.sentence[0:self.splitpoint], fg='grey', font=('calibri', 20))
        self.TextToWrite = tk.Label(
            self.window2, text=self.sentence[self.splitpoint:], font=('calibri', 20))

        self.timeElapsed = tk.Label(self.window2, text=f'0 seconds', fg="grey")
        self.LetterToWrite = tk.Label(
            self.window2, text=self.sentence[self.splitpoint], fg="grey")

        self.WrittenText.place(relx=0.5, rely=0.5, anchor=tk.E)
        self.TextToWrite.place(relx=0.5, rely=0.5, anchor=tk.W)
        self.timeElapsed.place(relx=0.5, rely=0.3, anchor=tk.N)
        self.LetterToWrite.place(relx=0.5, rely=0.7, anchor=tk.S)

        self.resultsbtn = ttk.Button(
            self.window2, text="Show Results", style='W.TButton', width=10, command=self.getResults)

        self.tryagainbtn = ttk.Button(
            self.window2, text="Try Again", style='W.TButton', width=10, command=self.tryagain)

        self.window2.bind("<Key>", self.keyPressed)

        self.window2.after(60000, self.stop)
        self.window2.after(1000, self.addSecond)

    def tryagain(self):
        self.window2.destroy()
        self.test_window()

    def keyPressed(self, event):

        try:
            if event.char.lower() == self.TextToWrite.cget('text')[0].lower() and self.TestOn:

                self.WrittenText.configure(text=self.String)
                self.TextToWrite.configure(text=self.TextToWrite.cget('text')[
                                           1:] + event.char.lower())
                self.String += event.char.lower()
                if self.TextToWrite.cget('text')[0].lower() == ' ':
                    self.LetterToWrite.configure(text='space', font=(10))
                else:
                    self.LetterToWrite.configure(
                        text=self.TextToWrite.cget('text')[0], font=(10))
            elif not self.TestOn:
                
                self.WrittenText.configure(text='Test ')
                self.TextToWrite.configure(text='finished !')
                self.LetterToWrite.configure(
                    text='Go check the results of the test')
                self.resultsbtn.place(relx=0.3, rely=0.85, anchor=tk.S)
                self.tryagainbtn.place(relx=0.7, rely=0.85, anchor=tk.S)

        except tk.TclError:
            pass

    # Se puede mejorar creando una base de datos con los resultados para presentar un leaderboard con las puntuación y una calificación.
    # Los resultados se pueden ir añadiendo a esa tabla igual incluso con la posibilidad de meter un nombre.
    def getResults(self):
        messagebox.showinfo(
            "Resultados", f'You typed a total of {len(self.String)} words out of {len(self.sentence)} words in a minute')

    def stop(self):
        self.TestOn = False
        self.totalwords = len(self.TextToWrite.cget('text').split(' '))

    def addSecond(self):
        self.passedSeconds = self.passedSeconds + 1
        self.timeElapsed.configure(text=f'{self.passedSeconds} Seconds')
        if self.TestOn:
            self.window2.after(1000, self.addSecond)
        if self.passedSeconds == 60:
            self.TestOn = False


if __name__ == "__main__":
    main_window = tk.Tk()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    App = Aplication(main_window)
    App.draw()
    App.mainloop()
