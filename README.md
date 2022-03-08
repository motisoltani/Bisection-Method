# Bisection Method-Python
The simplest root finding algorithm is the bisection method. This program implements Bisection Method for finding real root of nonlinear equation in python programming language. 
This program shows you table and graph related to the function and the root. I hope you find it useful.
<br /> Parameters
<br />----------
<br />f : function
<br />        The function for which we are trying to approximate a solution f(x)=0.
<br />xl , xu : numbers
<br />        The interval in which to search for a solution. The function returns
<br />        None if f(xl)*f(xu) >= 0 since a solution is not guaranteed.
<br />N : number of iterations
<br />eps : Acceptable Error
<br />Epsilon : (xm(new)-xm(old))/xm(new))*100
<br />xm : (xl-xu)/2
