#!/usr/bin/env python

from functools import partial
import Tkinter

root=Tkinter.Tk()
mylabel=Tkinter.Label(root,text='Welcome',font='Arial 20')

mybutton=partial(
    Tkinter.Button,
    root,
    foreground='white',
    background='blue',
    font='Arial 20'
                 )

b1=mybutton(text='Button 1')
b2=mybutton(text='Button 1')
qb=mybutton(foreground='red',text='quit',command=root.quit)

mylabel.pack()
b1.pack()
b2.pack()
qb.pack()
root.mainloop()