from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.insert(5,"Divertido: ")
def myClick():
	myLabel = Label(root,text = e.get())
	myLabel.pack()
myButton = Button(root,text = "Click Me",command = myClick)
myButton.pack()
root.mainloop()