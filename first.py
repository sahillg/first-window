import tkinter


sahil = tkinter.Tk()
# Code to add widgets will go here...
sahil.geometry("400x300")

def showt():
    text=tkinter.Label(text='hello guys , Welcome to the screen !')
    text.pack()

# create a toplevel menu
menubar = tkinter.Menu()
file=tkinter.Menu(menubar)
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label='file',menu=file)
edit=tkinter.Menu(menubar)
edit.add_command(label='Cut')
edit.add_command(label='copy')
edit.add_command(label='paste')
menubar.add_cascade(label='edit',menu=edit)

img=tkinter.Menu(menubar)
img.add_command(label="showImg")
img.add_command(label='showText',command = showt )
menubar.add_cascade(label='img',menu=img)



sahil.config(menu=menubar)
sahil.mainloop()
