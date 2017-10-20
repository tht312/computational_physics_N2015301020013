import matplotlib.pyplot as plt

g = 10
dt = 0.05
Vx = 70
x = [0] * 20
Vy1 = [5] * 20
y1 = [1] * 20
Vy2 = [5] * 20
y2 = [1] * 20
for i in range (0,19):    
    x[i+1] = x[i] + Vx * dt
    Vy1[i+1] = Vy1[i] - (0.00041 * 2000 / 60  * Vx) * dt - g * dt
    y1[i+1] = y1[i] + Vy1[i] * dt
    Vy2[i+1] = Vy2[i] - g * dt
    y2[i+1] = y2[i] + Vy2[i] * dt


plt.plot(x, y1,'b-.')
plt.plot(x, y2,'r-.')
plt.ylim(0, 3)
plt.xlabel("x") 
plt.ylabel("y")
plt.title('y-x relation') 
plt.legend(labels = ['spin', 'no spin'])
plt.show()