import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_cos(frame, line, x):
    # frame - параметр который меняется от кадра к кадру
    # в данном случае жто начальная фаза (угол)
    # line - ссылка на обьект line2D
    line.set_ydata(np.cos(x+frame))
    return [line]



#plt.ion()

fig, ax = plt.subplots()

x=np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)

line,=ax.plot(x,y)

phasa = np.arange(0, 4*np.pi, 0.1)
# for delay in np.arange(0, np.pi, 0.1):
#     #faza increase i dohodit do pi
#     y=np.cos(x+delay)
#
#     line.set_ydata(y)
#
#     #plt.clf() - polnoe cleaning
#
#     plt.draw()
#     plt.gcf().canvas.flush_events()
#
#     time.sleep(0.02)

animation = FuncAnimation(

    fig, #фигура где отображается анимация
    func = update_cos, #функция обновления текущего кадра
    frames =  phasa, #параметр, меняющийся от кадра к кадру
    fargs=(line,x), #доп параметры для функции апдейт_кос
    interval=30, # задержка между кадрами в мс
    blit=True, #использовать ли двойную буферизацию - обновление незаметно для пользователя
    repeat=False #зацикливать ли анимацию
)

#plt.ioff()
plt.show()