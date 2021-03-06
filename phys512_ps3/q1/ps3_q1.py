import numpy as np
import matplotlib.pyplot as plt

def rk4_step(func, x, y, h):
    
    k1 = func(x,y)  ##slop at initial point
    k2 = func(x+h/2, y+h*k1/2)  ##slope at midpoint, using k1
    k3 = func(x+h/2, y+h*k2/2)  ##slope at midpoint, using k2
    k4 = func(x+h, y+h*k3)  ##slope at endpoint, using k3
    yn = y + h*(k1/6 + k2/3 + k3/3 + k4/6) ##value of y at endpoint
    return yn
    
    
def rk4_stepd(func, x, y, h):
    
    ##stepsize = h
    k1 = func(x,y)              
    k2 = func(x+h/2, y+h*k1/2)
    k3 = func(x+h/2, y+h*k2/2)
    k4 = func(x+h, y+h*k3)
    yn1 = y + h*(k1/6 + k2/3 + k3/3 + k4/6)
    
    ##stepsize = h/2
    hn = h/2
    k1 = func(x,y)  ##k1 is the same
    k2 = func(x+hn/2, y+hn*k1/2)
    k3 = func(x+hn/2, y+hn*k2/2)
    k4 = func(x+hn, y+hn*k3)
    ymid = y + hn*(k1/6 + k2/3 + k3/3 + k4/6) ##ymid = y(x+h/2)!
    
    ##start from midpoint, need to reset (x,y)
    x = x + hn
    y = ymid
    k1 = func(x,y)
    k2 = func(x+hn/2, y+hn*k1/2)
    k3 = func(x+hn/2, y+hn*k2/2)
    k4 = func(x+hn, y+hn*k3)
    yn2 = y + hn*(k1/6 + k2/3 + k3/3 + k4/6) ##now at endpoint
   
    ##cancel out the leading-order error term 
    yc = (16*yn2-yn1)/15
    
    return yc


##use rk4_step or rk4_step to integrate func, return y_comp which contains the values of y calculated at each step
def y_comp(func, y0, x_array, integrator):
    y_comp = np.zeros(x_array.shape)
    y_comp[0] = y0
    h = x_array[1] - x_array[0] ##stepsize
    for i in range(0,len(x_array)-1):
        y_comp[i+1] = integrator(func, x_array[i], y_comp[i], h)
    
    return y_comp

    
    
    
    
##integrate dy/dx = y/(1+x**2) from x = −20 to x = 20 with y(−20) = 1 using 200 steps
dydx = lambda x, y: y/(1+x**2)
x_array = np.linspace(-20, 20, 201)

##analytic solution: y = c0 exp(arctan(x))
c0 = 1/(np.exp(np.arctan(-20)))
y = lambda x: c0*np.exp(np.arctan(x))
y_analytic = y(x_array)

##use RK4 integrator
y_cal1 = y_comp(dydx, 1, x_array, rk4_step)
y_cal2 = y_comp(dydx, 1, x_array, rk4_stepd)

##p3q1_f1.png
plt.clf()
plt.plot(x_array, y_analytic, label = 'analytic solution')
plt.plot(x_array, y_cal1, label = 'rk4_step')
plt.legend()
plt.show()

##p3q1_f2.png
plt.clf()
plt.plot(x_array, np.abs(y_analytic-y_cal1), label = 'analytic solution-rk4_step')
plt.legend()
plt.show()

##p3q1_f3.png
plt.clf()
plt.plot(x_array, y_analytic, label = 'analytic solution')
plt.plot(x_array, y_cal1, label = 'rk4_step')
plt.legend()
plt.show()
    
##p3q1_f4.png
plt.clf()
plt.plot(x_array, np.abs(y_analytic-y_cal2), label = 'analytic solution-rk4_stepd')
plt.legend()
plt.show() 

##p3q1_f5.png
plt.clf()
plt.plot(x_array, np.abs(y_cal1-y_cal2), label = 'rk4_step-rk4_stepd')
plt.legend()
plt.show() 