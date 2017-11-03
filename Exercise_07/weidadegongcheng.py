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
        self.x = [0.2] * 100000
        self.w = [0] * 100000
        self.t = [0] * 100000
        self.X = []
        self.W = []
        self.T = []
    def calculate(self):
        for i in range (0,99999):
            self.w[i+1] = self.w[i]-self.g/self.l*math.sin(self.x[i])*self.dt-self.q*self.w[i]*self.dt+self.F*math.sin(self.D*self.t[i])*self.dt
            self.x[i+1] = self.x[i] + self.w[i+1] * self.dt
            if self.x[i+1]>math.pi:
                self.x[i+1]=self.x[i+1]-2*math.pi
            elif self.x[i+1]<-math.pi:
                self.x[i+1]=self.x[i+1]+2*math.pi
            self.t[i+1]=self.t[i] + self.dt
        for i in range (0,99999):
            for j in range(0,444):
                if self.t[i]<0.5*self.dt+2*j*3.14/self.D and self.t[i]>-0.5*self.dt+2*j*3.14/self.D:
                    self.X.append(self.x[i])
                    self.W.append(self.w[i])
                    self.T.append(self.t[i])
                
            
a = exercise(1.4)
a.calculate()
b = exercise(1.44)
b.calculate()
c = exercise(1.465)
c.calculate()

plt.title('w ratio x') 
plt.figure(1) 
plt.plot(a.X, a.W,'b.')
plt.legend(labels = ['F=1.4'])
plt.figure(2)
plt.plot(b.X, b.W,'r.')
plt.legend(labels = ['F=1.44'])
plt.figure(3) 
plt.plot(c.X, c.W,'y.')
plt.legend(labels = ['F=1.465'])
plt.show()