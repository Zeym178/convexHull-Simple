import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig, ax = plt.subplots()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ax.set_xlim([0, 100])
ax.set_ylim([0, 100])

coor = []

def onclick(event):
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        ax.scatter(x, y, color='r')
        canvas.draw()
        coor.append((x, y))

def animate():
    global coor
    if len(coor) > 2:
        coor.sort()
        auxini = []

        ac1 = coor[0]
        ac2 = None
        ac3 = None

        if ac1[0] == coor[1][0]:
            ac2 = coor[1]
        else:
            for it in coor:
                if it[0] != ac1[0]:
                    pen = -(it[1] - ac1[1]) / (it[0] - ac1[0])
                    auxini.append((pen, it))
            auxini.sort()
            ac2 = auxini[0][1]

        fx = [ac1[0], ac2[0]]
        fy = [ac1[1], ac2[1]]

        while coor[0] != ac2:
            ma = -1
            f = 0
            for i in range(len(coor)):
                if coor[i] != ac1 and coor[i] != ac2:
                    ac3 = coor[i]
                    ta = (ac1[0] - ac2[0], ac1[1] - ac2[1])
                    tb = (ac3[0] - ac2[0], ac3[1] - ac2[1])
                    res = ((ta[0] * tb[0]) + (ta[1] * tb[1])) / (
                                (math.sqrt(ta[0] ** 2 + ta[1] ** 2)) * (math.sqrt(tb[0] ** 2 + tb[1] ** 2)))
                    res = math.acos(res) / math.pi * 180.0
                    if res > ma:
                        ma = res
                        f = i
            fx.append(coor[f][0])
            fy.append(coor[f][1])
            ac1 = ac2
            ac2 = coor[f]

        ax.plot(fx, fy, color='b')
        canvas.draw()

canvas.mpl_connect('button_press_event', onclick)

button = tk.Button(frame, text="Dibujar figura", command=animate)
button.pack(side=tk.BOTTOM)

root.mainloop()
