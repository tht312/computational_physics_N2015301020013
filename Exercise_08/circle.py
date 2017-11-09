import matplotlib.pyplot as plt
class exercise:
    def __init__(self,a):
        self.a = a
        self.x = [0.2] * 10000
        self.y = [0] * 10000
        self.Vx = [0.2] * 10000
        self.Vy = [0.5] * 10000
        self.dt = 0.01
    def calculate(self):
        for i in range (0,9999):
            self.x[i+1]=self.x[i]+self.Vx[i]*self.dt
            self.y[i+1]=self.y[i]+self.Vy[i]*self.dt
            self.Vx[i+1]=self.Vx[i]
            self.Vy[i+1]=self.Vy[i]
            if self.x[i+1]*self.x[i+1]+self.y[i+1]*self.y[i+1]/(1+self.a)/(1+self.a)>1:
                temp_x=(self.x[i]+self.x[i+1])/2
                temp_y=(self.y[i]+self.y[i+1])/2
                self.Vx[i+1]=(1-2*temp_x*temp_x)*self.Vx[i]-2*temp_x*temp_y*self.Vy[i]
                self.Vy[i+1]=(1-2*temp_y*temp_y)*self.Vy[i]-2*temp_x*temp_y*self.Vx[i]
        
a=exercise(0)
b=exercise(0.01)
c=exercise(0.02)
a.calculate()
b.calculate()    
c.calculate()
plt.figure(1)    
plt.plot(a.x, a.y,'b-.')
plt.figure(2)
plt.plot(b.x, b.y,'r-.')
plt.figure(3)
plt.plot(c.x,c.y,'g-.')
plt.show