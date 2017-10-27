import matplotlib.pyplot as plt
import math

class exercise:    
    def __init__(self,f):
        self.F = f
        self.g = 9.8
        self.l = 9.8
        self.q = 0.5
        self.D = 2/3
        self.dt = 0.04
        self.x = [0.2] * 1000
        self.w = [0] * 1000
        self.t = [0] * 1000
    def calculate(self):
        for i in range (0,999):
            self.w[i+1] = self.w[i]-self.g/self.l*math.sin(self.x[i])*self.dt-self.q*self.w[i]*self.dt+self.F*math.sin(self.D*self.t[i])*self.dt
            self.x[i+1] = self.x[i] + self.w[i+1] * self.dt
            if self.x[i+1]>math.pi:
                self.x[i+1]=self.x[i+1]-2*math.pi
            elif self.x[i+1]<-math.pi:
                self.x[i+1]=self.x[i+1]+2*math.pi
            self.t[i+1]=self.t[i] + self.dt
            
a = exercise(0.1)
a.calculate()
b = exercise(0.5)
b.calculate()
c = exercise(0.99)
c.calculate()

plt.title('x ratio time') 
plt.plot(a.t, a.x,'b-.')
plt.plot(a.t, b.x,'r-.')
plt.plot(a.t, c.x,'y-.')
plt.legend(labels = ['F=0.1', 'F=0.5','F=0.99'])
plt.show()