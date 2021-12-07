#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sklearn.datasets import load_iris
import numpy as np

def parse_data():
    dataset = load_iris()
    target = dataset.target
    target_names = dataset.target_names
    index, count = np.unique(target, return_counts=True)
    return target, count, target_names

root = Tk()
root.title("Pie")

fig, ax = plt.subplots()
target, count, target_names = parse_data()
ax.pie(count, labels = target_names)
canvas = FigureCanvasTkAgg(fig, master = root)  
canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()