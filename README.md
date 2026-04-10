# Pi-Thon

A Python simulation of Buffon's Needle problem to estimate the value of Pi using the Monte Carlo method.
This project of mine is based on the famous Monte Carlo Problem, of which this is the  simulation of Buffon’s Needle problem.
It has been designed as simplified model where L= 1.0 and D = 2.0. 

So basicaly this collapses the probability formula P= 2L/πD down to P= 1/π, therby reducing our calcuations.

In much simpler words The Buffon's Needle problem asks: If you drop a needle onto a floor with parallel lines, what is the probability that the needle will cross one of the lines?
In this simulation:

The Needle: A crispy French Fry (L=1.0).

The Grid: Lines on the griddle spaced exactly D=2.0 apart.


The simulation uses the following crossing condition to determine if a fry has touched a line:
if x <= (L/2) * abs(math.sin(theta)):


Language: Python

Web Framework: Streamlit 

Logic: random for stochastic sampling and math for trigonometric crossing conditions.



Using Python To find the value of Pi
