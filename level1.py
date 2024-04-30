import math

x1 = 2.5
y1 = -7
x2 = 4
y2 = 9.5

dif1 = x1-x2
dif2 = y1-y2

distance_squared = (dif1*dif1) + (dif2*dif2)
distance = math.sqrt(distance_squared)

print(distance)