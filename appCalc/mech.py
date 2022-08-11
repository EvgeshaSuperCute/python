from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from params import calc_entry, root
import math
import sys


def calc(key):
    global memory
    if key == "=":
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)