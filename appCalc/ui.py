from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mech import calc
import math
import sys


def setUI(bttn_list, root):

    r = 1
    c = 0
    for i in bttn_list:
        rel = ""
        cmd = lambda x=i: calc(x)
        ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
        c += 1
        if c > 4:
            c = 0
            r += 1