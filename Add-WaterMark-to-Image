import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Style
from PIL import ImageTk, Image, ImageDraw, ImageFont



class Aplication(tk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title('WaterMark')
        main_window.state('zoomed')
        self.menubar = tk.Menu(main_window, tearoff=False)
        main_window.configure(menu=self.menubar)

    def draw(self):
        self.frame = ttk.Frame(master=main_window)
        self.frame2 = ttk.Frame(master=self.frame)
        
        self.frame.pack(anchor=tk.CENTER)
        self.imageLabel = ttk.Label(master=self.frame2,text='',compound='bottom',font=('Helvetica','10'))

        self.canvas = tk.Canvas(master=self.frame, width=2600, height=1800)
        
        self.style = Style()
        self.style.configure('W.TButton', font=(
            'calibri', 10, 'bold', 'underline'))
        self.titlelabel = ttk.Label(
            master=self.frame, text="Watermark App", font=('castellar', 30))
        
        self.editMenu = tk.Menu(main_window, tearoff=False)
        self.filemenu = tk.Menu(main_window, tearoff=False)
        self.menubar.add_cascade(label='Edit picture', menu=self.editMenu)
        self.menubar.add_cascade(label='File',menu=self.filemenu)
        self.filemenu.add_command(label='Open file', underline=0,command=self.getImage)
        self.filemenu.add_command(label='Save file', underline=0,command=self.saveImage)
        
        self.editMenu.add_command(label='Add watermark',underline=0,command=self.addWatermark)
        self.titlelabel.pack(anchor=tk.N, pady=30)
        
        self.frame2.pack()
        self.canvas.pack(expand='yes', fill='both',anchor='center')
        self.imageLabel.pack()
        
    def getImage(self):

        path=filedialog.askopenfilename(filetypes=(('jpg file','*.jpg'),("png file", "*.png"), ("All Files", "*.*")))
        self.img = Image.open(path)
        self.resize_image =self.img.resize((1200, 630))
        self.image_original = ImageTk.PhotoImage(self.img)
        self.image_copy = ImageTk.PhotoImage(self.resize_image)
        self.canvas.create_image(1000, 300, anchor='center', image=self.image_copy)
       
    def saveImage(self):
        path = filedialog.asksaveasfilename(filetypes=(('jpg file','*.jpg'),("png file", "*.png")))
        self.img.save(path)

    def addWatermark(self):
        self.canvas.create_text(1540, 600, text='Watermark bruno', font=('Helvetica','10'), fill="white")
        
        self.drawImage = ImageDraw.Draw(self.img)
        font = ImageFont.truetype("arial.ttf", 15)
        self.drawImage.text((self.img.width-150, self.img.height - 30),'Watermark Bruno', (255,255,255) , font=font)
        

if __name__ == '__main__':
    main_window = tk.Tk()
    App = Aplication(main_window)
    App.draw()
    App.mainloop()
