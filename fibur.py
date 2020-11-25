#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline



def fibur(x,r,i):
	if i == 0: return x
	else: return r*fibur(x,r,i-1) * (1-fibur(x,r,i-1))


x0 = 0.5
n = 21
def fii(r):
	return fibur(x0,r,n)

def fii2(r): return fibur(x0,r,20)
def fii3(r): return fibur(x0,r,16)
def fii4(r): return fibur(x0,r,17)
def fii5(r): return fibur(x0,r,18)
def fii6(r): return fibur(x0,r,19)

minbound = 0
maxbound = 4
breadth = 0.001
x = np.arange(minbound,maxbound,breadth)
y = fii(x)
y2 = fii2(x)



plt.figure(figsize=(15,5))
plt.plot(x,y,'k')
plt.plot(x,y2,'k')
plt.plot(x,fii3(x),'k')
plt.plot(x,fii4(x),'k')
plt.plot(x,fii5(x),'k')
plt.plot(x,fii6(x),'k')
plt.title('x_(n+1) = r * x(n) * (1-x(n))',fontsize=17)
plt.xlabel('r',fontsize=16)
plt.ylabel('x(20)',fontsize=16)
plt.legend(['n = 21', 'n = 20','n = 22', 'n = 23','n = 24', 'n = 25'])

plt.show()
