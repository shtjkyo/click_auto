import tkinter


class Tkwin:
    def __init__(self, root):
        self.root = root
        self.frame = tkinter.Frame(root, bd=2)
        self.edit = tkinter.Text(self.frame, width=1152, height=864)
        self.edit.pack(side=tkinter.LEFT)
        self.frame.place(y=0)
        self.edit.bind('<Button-1>', self.action)

    def action(self, event):
        self.edit.insert(tkinter.END, "Window_location x:%d y:%d\n" % (event.x, event.y))
        self.edit.insert(tkinter.END, "Screen_location x:%d y:%d\n" % (event.x_root, event.y_root))


root = tkinter.Tk();
root.overrideredirect(True)
window = Tkwin(root)
root.minsize(1152, 864)
root.maxsize(1152, 864)
root.mainloop()
