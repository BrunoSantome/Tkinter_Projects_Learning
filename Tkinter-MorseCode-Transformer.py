import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style


class Aplication(tk.Frame):
    def __init__(sel, main_window):
        super().__init__(main_window)
        main_window.title('Morse code transformer')
        main_window.state('zoomed')

    def draw(self):
        self.mainframe = ttk.Frame(main_window)
        self.mainframe.pack(anchor=tk.CENTER, pady=10)

        self.titlelabel = ttk.Label(
            self.mainframe, text="Morse Code Transformer", font=('castellar', 30))

        self.explainLabel = ttk.Label(
            self.mainframe, text='Please enter the text you want to transfrom below', font=('castellar', 10))
        self.textEntry = tk.Entry(master=self.mainframe, bd=4, width=100)
        self.style = Style()
        self.style.configure('W.TButton', font=(
            'calibri', 10, 'bold', 'underline'))
        self.transormBtn = ttk.Button(
            master=self.mainframe, text='Transform Text', width=20, command=self.getMorse)

        self.MorseLabel = ttk.Label(master=self.mainframe, width=10, font=('castellar', 20))
        
        self.explainLabel2 = ttk.Label(master=self.mainframe, width=50, font=('castellar', 12),text='The input in Morse code would be: ')
        self.titlelabel.pack(anchor=tk.CENTER, pady=10)
        self.explainLabel.pack(anchor=tk.CENTER, pady=10)
        self.textEntry.pack(anchor=tk.CENTER, pady=10)
        self.transormBtn.pack(anchor=tk.CENTER, pady=10)
        
        
    def getMorse(self):
        self.initiatedict()
        parsed_entry = self.textEntry.get().upper()
        Morsecode = ''
        for letter in parsed_entry:
            Morsecode += self.LETTERS_TO_MC[letter]
        self.explainLabel2.pack(anchor=tk.CENTER, pady=10)
        self.MorseLabel.pack(anchor=tk.CENTER, pady=10)
        self.MorseLabel['text'] = Morsecode


    def initiatedict(self):
        self.LETTERS_TO_MC = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ' ': '/'
        }


if __name__ == '__main__':
    main_window = tk.Tk()
    app = Aplication(main_window)
    app.draw()
    app.mainloop()
