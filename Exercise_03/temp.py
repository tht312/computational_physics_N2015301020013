import matplotlib.pyplot as plt
def velocity(time):
    if time == 0:
        return 0
    else:
        return velocity(time-0.1)+(10-1*velocity(time-0.1))*0.1
v = []
for i in range(0,3):
    s = velocity(0.1*i)
    v.append(s)
t = []
for i in range(0,3):
    s = 0.1*i
    t.append(s)
plt.plot(t, v,'o')
plt.show()