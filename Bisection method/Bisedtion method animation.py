'''
Bisection Method 
language: Python

Motahare Soltani 

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
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

fig = figure(figsize=(8, 8), dpi=120)


# Define the function whose roots are required
def f(x):
    return (x**3) - 0.165 * (x**2) + 3.9993 * (10**(-4))

# Input Parameters
N = 50           # Max. number of iterations
eps = 5       # Acceptable Error 
xl = 0           # Guess Value for the lower bound on the root
xu = 0.11        # Guess Value for the upper bound on the root

# Plot the given function
x = np.arange(xl-0.5,xu+0.5,0.00001)
y = f(x)
plt.plot(x,y, linewidth=3)
plt.axhline(y=0, c='black',linewidth=1)

if f(xl)*f(xu) >= 0:
        print("Bisection method fails.")

# Print the table header
print('------------------------------------------------------------------------------------------------')
print('iter \t\t xl \t\t xu \t\t xm \t\t Epsilon% \t f(xm)        ')
print('------------------------------------------------------------------------------------------------')

xm_list = []
Epsilon = [100]

for i in range(N):
        xm = (xl+xu)/2
        xm_list.append(xm)

        # Plot the important points and annotate them on the graph
        # Title
        plt.title(r"$\bf{ITERATION} $ #"+str(i+1)+'\n\na = % 10.8f;       b = % 10.8f;      c = ?;       f(c) = ?'%(xl, xu))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.rcParams.update({'font.size': 10})
        
        ax = plt.gca() # grab the current axis
        
        # Create a secondary axis for marking the a,b and c points
        secondary_ax = ax.secondary_xaxis('top')
        labels2 = [item.get_text() for item in secondary_ax.get_xticklabels()]
        ticks = plt.xticks()[0]
        labels2=['xl','xu']
        secondary_ax.set_xticks( [xl,xu])
        secondary_ax.set_xticklabels(labels2)
        plt.scatter(xl,f(xl),c='blue',s=250,alpha=0.5)
        plt.scatter(xu,f(xu),c='blue',s=250,alpha=0.5)
        
        plt.annotate('f(xl)',[xl,f(xl)])
        plt.annotate('f(xu)',[xu,f(xu)])
        
        plt.axvline(x=xl, c='blue',linewidth=2,alpha=0.5)
        plt.axvline(x=xu, c='blue',linewidth=2,alpha=0.5)
        plt.pause(2.0)

        plt.rcParams.update({'font.size': 9})
        plt.title(r"$\bf{ITERATION} $ #"+str(i+1)+'\n\nxl = % 10.8f;       xu = % 10.8f;      xm = % 10.8f;       f(xm) = % 10.8f'%(xl, xu, xm, f(xm)))
        plt.rcParams.update({'font.size': 10})
        plt.annotate('f(xm)',[xm,f(xm)])
        labels2 = [item.get_text() for item in secondary_ax.get_xticklabels()]
        ticks = plt.xticks()[0]
        labels2=['xl','xu','xm=(xl+xu)/2']
        secondary_ax.set_xticks( [xl,xu,xm])
        secondary_ax.set_xticklabels(labels2)
           
        plt.scatter(xm,f(xm),c='red',s=250,alpha=0.5)
        
        plt.axvline(x=xm, c='red',linewidth=2,alpha=0.5)
        plt.autoscale()
        
        plt.pause(2.0)
       

        if f(xm) == 0:
                print('Root found : ' +str(xm))
        elif i >= 1:
                Epsilon.append((abs((xm_list[i]-xm_list[i-1])/xm_list[i])*100))
                print(str(i+1)+'\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' %(xl, xu, xm, Epsilon[i], f(xm)))
        else:
                print(str(i+1)+'\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' %(xl, xu, xm, Epsilon[i], f(xm)))   

        if Epsilon[i] < eps:
                print('------------------------------------------------------------------------------------------------')
                print('Root found : '+str(xm_list[i]))
                text = plt.text(0.5, 0.5, 'Root found.\n\n Epsilon% = '+str(np.round(Epsilon[i],5))+'\n\nRoot ≈'+str(np.round(xm,7))+'\n\nf(xm) ='+str(f(xm)), fontsize=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
                # Change opacity of the text box
                text.set_bbox(dict(facecolor='papayawhip', alpha=0.6, edgecolor='papayawhip'))
                plt.pause(5.0)
                break
        
                
        elif f(xl)*f(xm)<0:
                #Plot
                text = plt.text(0.5, 0.2, 'f(xl).f(xm)<0\n\n xu=xm', fontsize=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
                text.set_bbox(dict(facecolor='whitesmoke', alpha=0.5, edgecolor='whitesmoke'))
                plt.scatter(xl,f(xl),c='yellow',s=175,alpha=1)
                plt.scatter(xm,f(xm),c='yellow',s=175,alpha=1)
                plt.pause(2.0)
                # Change the upper bound
                xu = xm                                
        else:
                #Plot
                text = plt.text(0.5, 0.2, 'f(xm).f(xu)<0\n\n xl=xm', fontsize=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
                text.set_bbox(dict(facecolor='whitesmoke', alpha=0.5, edgecolor='whitesmoke'))
                plt.scatter(xu,f(xu),c='yellow',s=175,alpha=1.0)
                plt.scatter(xm,f(xm),c='yellow',s=175,alpha=1)
                plt.pause(1)
                # Change the lower bound
                xl = xm
                plt.pause(2.0)
        plt.clf()
        x = np.arange(xl-(xu-xl)/2,xu+(xu-xl)/2,0.00001)
        y = f(x)
        plt.rcParams.update({'font.size': 10})
        plt.plot(x,y, linewidth=3)
        plt.axhline(y=0, c='black',linewidth=1)        

plt.show()
print('--------------------------------------------------------------------------')
                
                        
                        





