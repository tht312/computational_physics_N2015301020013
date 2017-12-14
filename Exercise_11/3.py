import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.3
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
f, ax = plt.subplots()
ax = plt.axes(title = 'Waves on a string\n(fixed ends)',xlim = (0,1), ylim = (-5,5),xlabel = 'x (m)',ylabel = 'y (m)') 
p, = ax.plot([],[])
x = np.arange(0,1 + Delta_x,Delta_x)
def animate(i):
    X = x
    Y = y[i]
    p.set_data(X,Y)  
    return p,  
gif = animation.FuncAnimation(f,animate,interval=50)
plt.show()