import os
from tkinter import *
from PIL import ImageTk, Image


def nextImage():
    global counter
    img_display.config(image=img_array[counter % len(img_array)])
    counter += 1


counter = 1
root = Tk()
root.title('Gallery')
root.geometry('400x400')
root.configure(bg='black')

files = os.listdir('pictures')

img_array = []
for file in files:
    img = Image.open(os.path.join('pictures', file))
    img_array.append(ImageTk.PhotoImage(img))

img_display = Label(root, image=img_array[0])
img_display.pack(pady=(15, 10))

next_btn = Button(root, text='Next', bg='white', fg='black', width=20, height=2, command=nextImage)
next_btn.pack()

root.mainloop()
