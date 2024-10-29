from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry('500x500')
root.config(bg='lightblue')

num1 = StringVar()
num2 = StringVar()
operation = StringVar()
num3v = StringVar()

num3v.set('')

Label(root, text='Number1', bg='lightblue').grid(row=0, column=0)
Entry(root, textvariable=num1, bg='lightyellow').grid(row=0, column=1)
Label(root, text='Number2', bg='lightblue').grid(row=1, column=0)
Entry(root, textvariable=num2, bg='lightyellow').grid(row=1, column=1)
Label(root, text='operation', bg='lightblue').grid(row=2, column=0)
Entry(root, textvariable=operation, bg='lightyellow').grid(row=2, column=1)

def savetodb():
    num1v = num1.get()
    num2v = num2.get()
    operationv = operation.get()

    if operationv == '+':
        num3v.set(float(num1v) + float(num2v))
    elif operationv == '-':
        num3v.set(float(num1v) - float(num2v))
    elif operationv == '*':
        num3v.set(float(num1v) * float(num2v))
    elif operationv == '/':
        num3v.set(float(num1v) / float(num2v))
    else:
        root.destroy()

Button(root, text='result', command=savetodb, bg='lightgreen').grid(row=3, column=1)
Entry(root, textvariable=num3v, bg='lightyellow').grid(row=4, column=1)

root.mainloop()
