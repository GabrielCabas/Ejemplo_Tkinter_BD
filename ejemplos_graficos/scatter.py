#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sklearn.datasets import load_iris
def parse_data():
    dataset = load_iris()
    data = dataset.data
    features = dataset.feature_names
    return features, data

root = Tk()

fig, ax = plt.subplots()
features, data = parse_data()
sepal_length = [i[0] for i in data]
petal_length = [i[2] for i in data]
ax.scatter(sepal_length, petal_length, alpha=0.8, c="skyblue")
ax.set_xlabel("Sepal length")
ax.set_ylabel("Petal length")
canvas = FigureCanvasTkAgg(fig, master = root)  
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()

