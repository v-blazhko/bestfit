import matplotlib.pyplot as plt
from collections import Counter
import math
import numpy as np

# Lists multiplying func
def list_mult(list1, list2):
    result = [x * y for x, y in zip(list1, list2)]
    return result

# Displaying func
def func(x,a,b):
    return [i*a+b for i in x]
  
# Best Fit Line
def linfit(x_numbers, y_numbers):
    x_sum = sum(x_numbers)

    y_sum = sum(y_numbers)

    n = len(x_numbers)

    x_squared_sum = sum([i**2 for i in x_numbers])

    squared_x_sum = x_sum**2

    xy_sum=sum(list_mult(x_numbers,y_numbers))
    print("x_sum = "+str(x_sum))
    print("y_sum = "+str(y_sum))
    print(list_mult(x_numbers,y_numbers))
    print("xy_sum = "+str(xy_sum))
    print("x_squared_sum = "+str(x_squared_sum))
    print("n = " + str(n))

    print("x_n")
    print(x_numbers)
    print("y_n")
    print(y_numbers)


    a = (n*xy_sum - x_sum*y_sum)/(-x_sum**2 + x_squared_sum*n)
    b = (x_squared_sum*y_sum - x_sum*xy_sum)/(-x_sum**2 + x_squared_sum*n)

    print('a='+ str(a))
    print('b='+ str(b))
    
    plt.clf()
   
    # Numbers for X
    x = [i for i in range(int(math.floor(min(x_numbers))), int(math.ceil(max(x_numbers)))+1)]
    # Numbers for Y
    y = func(x,a,b)

    plt.title("y="+str(round(a,2))+"*x + " + str(round(b,2))+ " plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.plot(x, y, 'r')

    # Adding a grid
    plt.grid(True, linestyle='-', color='0.75')
    plt.scatter(x_numbers, y_numbers, edgecolors='r', s=10)
    plt.show()

#Event for clicking to add a point
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    x_numbers.append(float(event.xdata))
    y_numbers.append(float(event.ydata))
    if ((len(x_numbers)>1) and (len(y_numbers)>1)):
       linfit(x_numbers,y_numbers)
    else:
       plt.scatter(x_numbers, y_numbers, edgecolors='r', s=10)
       plt.show()


fig, ax = plt.subplots()
x_numbers = []
y_numbers = []

print('Please enter x-values')
x_numbers = [float(i) for i in input().split()]
print('Please enter y-values (same amount as x-values)')
y_numbers = [float(i) for i in input().split()]

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.grid(True, linestyle='-', color='0.75')

if ((len(x_numbers)>1) and (len(y_numbers)>1)):
    linfit(x_numbers,y_numbers)
else:
    plt.ylim(-1,10)
    plt.xlim(-1,10)
    plt.show()
