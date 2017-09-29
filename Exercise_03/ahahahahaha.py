import matplotlib.pyplot as plt
a = 10
b = 1
dt = 0.1
v = [0] * 30
for i in range (0,29):
    v[i+1]=v[i]+(a-b*v[i])*dt
t = [0] * 30
for i in range (0,29):
    t[i+1] = t[i] + dt
plt.plot(t, v,'b-.')
plt.xlabel("t") 
plt.ylabel("v")
plt.title('v-t relation') 
plt.show()