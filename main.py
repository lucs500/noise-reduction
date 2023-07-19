import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.signal import savgol_filter

df = pd.read_csv(r'C:\lo\ca\tion.csv') #reads input & output data

x = np.linspace(-1, 69, 69) #where 69 is the number corresponding to the volume of inputs
y = df['Output']

y_2 = df['Input']

y_filtered = savgol_filter(y, 99, 3) #applies savitzky-golay filter

fig = plt.figure()
ax = fig.subplots()
p, = ax.plot(x, y_filtered, 'g-')
ax.set_ylabel('Output filtered', color = 'g')
ax2 = ax.twinx()
ax2.plot(x, y_2, 'b-')
ax2.set_ylabel('Input', color = 'b')

plt.subplots_adjust(bottom=0.25)
ax_slide = plt.axes([0.25, 0.1, 0.65, 0.01])
win_len = Slider(ax_slide, 'Window length', valmin=5, valmax=99, valinit=99, valstep=2) #slider for filter parameters
def update(val):
    current_v = int(win_len.val)
    new_y = savgol_filter(y, current_v, 3)
    p.set_ydata(new_y)
    fig.canvas.draw()

win_len.on_changed(update)
plt.show() #plot
