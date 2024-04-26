import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation

# def update_cos(frame, line, x):
#     # frame - параметр который меняется от кадра к кадру
#     # в данном случае жто начальная фаза (угол)
#     # line - ссылка на обьект line2D
#     line.set_ydata(np.cos(x+frame))
#     return [line]

fig = plt.figure(figsize=(9,9))
ax_3d =  fig.add_subplot(projection='3d')

#INSTEAD OF X = NP.ARANGE AND Y = NP.COS(X) AND LINE, = AX.PLOT(X.Y):

x=np.arange(-2*np.pi, 2*np.pi, 0.1)
y=np.arange(-2*np.pi, 2*np.pi, 0.1)
xgrid, ygrid = np.meshgrid(x,y)
# формирование сетки для отображения 3ех мерного графика

phasa = np.arange(0, 2*np.pi, 0.05)
frames = [] #empty list

for p in phasa:
    zgrid = np.sin(xgrid+p)*np.sin(ygrid)/(xgrid*ygrid)
    line=ax_3d.plot_surface(xgrid,ygrid,zgrid, color='c')
    frames.append([line])

animation = ArtistAnimation(
    fig, #фигура где отображается анимация
    frames, #кадры
    interval=30, #задержка между кадрами в мс
    blit=True, #двойная буферизация
    repeat=True #зацикливание анимации
)

#plt.ioff()
plt.show()