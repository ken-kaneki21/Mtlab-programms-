import math as ma
import matplotlib.pyplot as plt
l1 = 7.9
l2 = 4.3
l3 = 6
theta_start = 0
theta_end = ma.pi/2
n_theta = 10
theta_1 = []
theta_2 = []
theta_3 = []
x0 = 0
y0 = 0
for i in range(0, n_theta):
 theta_value = theta_start + i*(theta_end-theta_start)/(n_theta-1)
 theta_1.append(theta_value)
 theta_2.append(theta_value)
 theta_3.append(theta_value)
 k = 1
for i in theta_1:
    for j in theta_2:
        for k in theta_3:
            x1 = l1*ma.cos(i)
            y1 = l1*ma.sin(i)
            x2 = x1+l2*ma.cos(j)
            y2 = y1+l2*ma.sin(j)
            x3 = x2+l3*ma.cos(k)
            y3 = y2+l3*ma.sin(k)
            filename = str(k) + '.png'
            k = k+1
            print(filename)
            plt.figure(1)
            plt.plot([x0, x1], [y0, y1], '-og')
            plt.plot([x1, x2], [y1, y2], '-or')
            plt.plot([x2, x3], [y2, y3], '-ob')
plt.show()