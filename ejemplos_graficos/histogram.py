#https://matplotlib.org/stable/plot_types/stats/hist_plot.html#sphx-glr-plot-types-stats-hist-plot-py
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sklearn.datasets import load_iris

root = Tk()
root.title("Histogram")

def parse_data():
    dataset = load_iris()
    data = dataset.data
    features = dataset.feature_names
    return features, data

fig, ax = plt.subplots()
features, data = parse_data()
sepal_length = [i[0] for i in data]

ax.hist(sepal_length, bins=10)
ax.set_xlabel("Sepal length")
canvas = FigureCanvasTkAgg(fig, master = root)  
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
