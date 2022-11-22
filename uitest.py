from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(400, 300)

        self.labelFrame = ttk.LabelFrame(self, text = "Choose your image")
        self.labelFrame.grid(column = 0, row = 1, padx = 0, pady = 20)

        self.button()

        #button
        btn2 = Button(text="Change lipstick color").place(x=145, y=100)
        btn3 = Button(text="Change eyes color").place(x=150, y=150)



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)


    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(img)

        self.label2 = Label(image=photo)
        self.label2.image = photo 
        self.label2.grid(column=3, row=4)



root = Root()
root.mainloop()