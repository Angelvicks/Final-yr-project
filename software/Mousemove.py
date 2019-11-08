from tkinter import *
from tkinter.colorchooser import askcolor
import sys, os, string, time


class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
    self.root = Tk()
    self.pen_button = Button(self.root, text='pen', command=self.use_pen)
    self.pen_button.grid(row=0, column=0)

    self.brush_button = Button(self.root, text='label', command=self.use_brush)
    self.brush_button.grid(row=0, column=1)

    self.color_button = Button(self.root, text='color', command=self.choose_color)
    self.color_button.grid(row=0, column=2)

    self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
    self.eraser_button.grid(row=0, column=3)

    self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
    self.choose_size_button.grid(row=0, column=4)

    self.canvas = Canvas(self.root, bg='white', width=1000, height=1000, highlightthickness=10)

    self.canvas.label = Listbox(self.root)
    self.canvas.label.insert(0, 'Object 1 has triangles')
    self.canvas.label.insert(1, 'Object 2 has schools')
    self.canvas.label.insert(2, 'Object 3 has courses')
    self.canvas.label.insert(3, 'Arrow 1 is getschool()')
    self.canvas.label.insert(4, 'Arrow 2 is showcourses()')
    self.canvas.label.insert(5, 'Arrow 3 is trianglewidth()')
    widget = Label(self.canvas, text='Attributes', fg='white', bg='black')
    self.canvas.create_window(100, 200, anchor=NW, window=widget)
    self.canvas.grid(row=1, columnspan=5,)
    self.canvas.create_window(10, 10, anchor=NW, window=self.canvas.label)
    self.canvas.create_line(575, 200, 315, 200, width=2, fill='black', arrow='first', activefill='violet', tags="DnD")
    self.canvas.create_oval(400, 400, 200, 200, width=2, fill='green', activefill='gray', tags="DnD")
    self.canvas.create_oval(700, 400, 500, 200, width=2, fill='blue', activefill='red', tags="DnD")
    self.canvas.create_oval(550, 600, 350, 400, width=2,fill='orange', activefill='yellow', tags="DnD")
    self.canvas.create_line(400, 415, 360, 380, width=2, fill='black', arrow='last', activefill='blue', tags="DnD")
    self.canvas.create_line(505, 415, 540, 380, width=2, fill='black', arrow='first', activefill='sky blue', tags="DnD")

    self.defaultcolor = self.canvas.itemcget(self.canvas.create_text(300, 415,font=("Helvetica", 14), text="Object 1", tags="DnD"),
                                            "fill")
    self.canvas.create_text(600, 415,
                           font=("Helvetica", 14), text="Object 2", tags="DnD")
    self.canvas.create_text(450, 615,
                           font=("Helvetica", 14), text="Object 3", tags="DnD")
    self.canvas.create_text(450, 180,
                           font=("Helvetica", 14), text="Arrow 1", tags="DnD")
    self.canvas.create_text(402, 380,
                      font=("Helvetica", 14), text="Arrow 2", tags="DnD")
    self.canvas.create_text(500, 380,
                      font=("Helvetica", 14), text="Arrow 3", tags="DnD")
        # Bind mouse events to methods (could also be in the constructor)
    self.canvas.bind("<Button-1>", self.select)
    self.canvas.bind("<B1-Motion>", self.drag)
    self.root.mainloop()

  def select(self, event):
    widget = event.widget                       # Get handle to canvas
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)

  def activate_button(self, some_button, eraser_mode=False):
    self.active_button.config(relief=RAISED)
    some_button.config(relief=SUNKEN)
    self.active_button = some_button
    self.eraser_on = eraser_mode

  def use_pen(self):
    self.activate_button(self.pen_button)

  def use_brush(self):
    self.activate_button(self.brush_button)

  def choose_color(self):
    self.eraser_on = False
    self.color = askcolor(color=self.color)[1]

  def use_eraser(self):
    self.activate_button(self.eraser_button, eraser_mode=True)

if __name__ == '__main__':
    # Get an instance of the MouseMover object
    MouseMover()
