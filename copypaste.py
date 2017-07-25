#! python2.7
from Tkinter import *
import tkMessageBox


master = Tk()
padx = 10
pady = 10


def copy_fields():
	master.clipboard_clear()
	master.clipboard_append(e2.get())
	tkMessageBox.showinfo(e2.get(), "Button Created")

def create_button():
	row = 3
	column = 3
	Button(master,text=e1.get(),command=create_button).grid(row=row,
		column=column,padx=padx, pady=pady, sticky=W)
	column = column + 1
	row = row + 1

Label(master, text="New Button Label").grid(row=0)
Label(master, text="Text to Copy").grid(row=1)


e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3,
	column=0, sticky=W, padx=padx, pady=pady)
Button(master, text='Create Button', command=lambda:[create_button(),
	copy_fields()]).grid(row=3,column=1,sticky=W, padx=padx, pady=pady)

mainloop()