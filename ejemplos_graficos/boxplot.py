#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sklearn.datasets import load_iris
root = Tk()
root.title("Boxplot")
def parse_data():
    dataset = load_iris()
    data = dataset.data
    features = dataset.feature_names
    return features, data

fig, ax = plt.subplots()
features, data = parse_data()
ax.boxplot(data, labels=features, vert=False)
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master = root)  
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
