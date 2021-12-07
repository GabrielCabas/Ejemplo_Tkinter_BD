#https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np

root = Tk()
root.title("Line")

fig, ax = plt.subplots()
x = np.linspace(-20, 20, 500)
sin = np.sin(x)
cos = np.cos(x)
ax.plot(x, sin, color="red", label="y = sin(x)")
ax.plot(x, cos, color="blue", label="y = cos(x)")
plt.legend(loc="upper right")
ax.set_xlabel("x")
ax.set_ylabel("y")
canvas = FigureCanvasTkAgg(fig, master = root)  
canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()