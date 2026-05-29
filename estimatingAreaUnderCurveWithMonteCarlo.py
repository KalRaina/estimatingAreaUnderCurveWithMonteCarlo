import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 4*x**2 + 3*x + 2

lowerLimit = float(input("Type in lower limit of integration: "))
upperLimit = float(input("Type in upper limit of integration: "))

x_interval = np.linspace(lowerLimit, upperLimit, 2000) # generates 2000 evenly spaced values between limits for smooth curve
y_interval = f(x_interval)

y_min = min(0, y_interval.min()) # smallest y value
y_max = max(0, y_interval.max()) # smallest x value

plt.plot(x_interval,y_interval) # plots the curve

plt.xlabel("x")
plt.ylabel("y")

plt.axhline(0,
            color = "black",
            linewidth = 1) # y axis

plt.axvline(0, 
            color ="black",
            linewidth = 1) # x axis

list = [] # will store estimates to calculate mean

for i in range (300): 
 
 N = 40000
 
 x2 = np.random.uniform(lowerLimit,upperLimit,N) # random generation of 400,000 values between limits on a uniform distribution

 y2 = np.random.uniform(y_min, y_max, N)

 inside = (y2 <= f(x2)) & (y2 >= 0) # below curve, above x axis
 otherinside = (y2 >= f(x2)) & (y2 <= 0) # above curve, below x axis

  # estimates area under curve via ratios between areas

 box_area = (upperLimit-lowerLimit) * (y_max - y_min) # area of box of plotting

 area = (inside.sum()-otherinside.sum())/N * (box_area) # finds area by using ratios

 list.append(area)

plt.scatter(x2[inside], y2[inside], s=1, color = "blue") # plots points that are classed as inside as blue
plt.scatter(x2[otherinside], y2[otherinside], s=1, color = "purple")
plt.scatter(x2[(~inside) & (~otherinside)], y2[(~inside) & (~otherinside)], s=1, color="red") # plots points that are outside as red

list = np.array(list) # so mean() will work

print(np.mean(list)) # prints mean

plt.grid(True)
plt.show()