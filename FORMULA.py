import numpy as np
import matplotlib.pyplot as plt
p=np.random.random(25)
y=np.random.random(25)
def LOGLOSS(p,y):
    k=np.log(p)
    l=np.log(1-p)
    return np.mean(-1*(y*k + (1-y)*l))

print(LOGLOSS(p,y))
#MISSING VALUES
a=np.array([1,2,3,np.nan,4,5])
print(a[~np.isnan(a)])
x=np.linspace(-10,10,100)
y=x
z=x**2
c=np.sin(x)
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,c)
plt.show()


