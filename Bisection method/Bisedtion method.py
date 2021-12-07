'''
Bisection Method 
language: Python

Motahare Soltani
soltani.wse@gmail.com 

Parameters
----------
f : function
        The function for which we are trying to approximate a solution f(x)=0.
xl , xu : numbers
        The interval in which to search for a solution. The function returns
        None if f(xl)*f(xu) >= 0 since a solution is not guaranteed.
N : number of iterations

eps : Acceptable Error

Epsilon : (xm(new)-xm(old))/xm(new))*100

xm : (xl-xu)/2

'''

import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


# Define the function whose roots are required
def f(x):
    return np.exp(-x) - np.cos(x)

# Input Parameters
N = 50           # Max. number of iterations
eps = 1     # Acceptable Error 
xl = 1        # Guess Value for the lower bound on the root
xu = 2       # Guess Value for the upper bound on the root

if f(xl) * f(xu) >= 0:
        print("Bisection method fails.")

# Input lists
xm_list = []
Epsilon = [100]
xl_list = [xl]
xu_list = [xu]
f_list = []


for i in range(N):
        xm = (xl + xu) / 2
        xm_list.append(xm)
        f_list.append(f(xm))
                
        if f(xm) == 0:
                print('Root found : ' +str(xm))
        elif i >= 1:
                Epsilon.append((abs( (xm_list[i] - xm_list[i-1]) / xm_list[i]) * 100))
                  
        if Epsilon[i] < eps:
                break        
        elif f(xl) * f(xm) < 0:
                xu = xm
                xl_list.append(xl)
                xu_list.append(xu)                                        
        else:
                xl = xm
                xl_list.append(xl)
                xu_list.append(xu)



# Table
columns = ["Iteration", "xl", "xu", "xm", "Epsilon%", "f(xm)"]
  
Table = PrettyTable()
  
# Add Columns
Table.add_column(columns[0], range(1,i+2))
Table.add_column(columns[1], [round(num, 4) for num in xl_list][:i+1])
Table.add_column(columns[2], [round(num, 4) for num in xu_list][:i+1])
Table.add_column(columns[3], [round(num, 4) for num in xm_list][:i+1])
Table.add_column(columns[4], [round(num, 4) for num in Epsilon][:i+1])
Table.add_column(columns[5], [round(num, 8) for num in f_list][:i+1])

print(Table)
print('Root found : '+str(xm_list[i]))
  

#Plot
fig = figure(figsize=(8, 8), dpi=75)
plt.subplot(2,1,1)
x = np.arange(xl-0.5,xu+0.5,0.00001)
y = f(x)
font1 = {'color':'blue','size':15}

plt.annotate('Root ≈ '+str(np.round(xm,5)), xy=(xm, f(xm)),xytext=(xm+0.1, f(xm)+0.05), arrowprops=dict(facecolor='blue', shrink=0.05))
plt.plot(x, y, 'b-', linewidth=3)
plt.scatter(xm,f(xm), c='purple', s=100,alpha=0.5)
plt.xlabel('X', fontsize=12)
plt.ylabel('Function', fontsize=12)
plt.title('y = f(x)', fontdict=font1, loc='left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.subplot(2,1,2)
x = np.arange(1,i+2)
y = Epsilon
font2 = {'color':'red','size':15}
text = plt.text((i+2)/2, 50, 'Epsilon% = '+str(np.round(Epsilon[i],5))+'\n\nRoot ≈'+str(np.round(xm,7))+'\n\nf(xm) ='+str(np.round(f(xm),10)), fontsize=16,horizontalalignment='center',verticalalignment='center')
text.set_bbox(dict(facecolor='papayawhip', alpha=0.6, edgecolor='papayawhip'))
plt.plot(x, y, 'r-', linewidth=3)
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Error(%)', fontsize=12)
plt.title('Convergence Diagram', fontdict=font2, loc='left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()
   
                        
                        





