from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
        self.quitButton=Button(self,text='Quit',command=root.destroy)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'word'
        messagebox.showinfo('Message','Hello,%s'%name)


root=tk.Tk()       
app = Application(master=root)
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()