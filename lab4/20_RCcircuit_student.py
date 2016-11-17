#
# RC circuit discharge
#
from visual import *
from visual.graph import *

# set up graphical output for charge
charge = gdisplay(title = 'Charge on capacitor vs. time', x=0, y=0, xmax=150,
                  xtitle = 't, s', ytitle = 'Q, Coulombs', ymax=3.0, height=300,
                  background=color.black)
Qgraph = gcurve(gdisplay=charge, color = color.cyan)


# set up graphical output for current
current = gdisplay(title = 'Current vs. time', x=0, y=400, xmax=150, ymax=.2,
                   xtitle = 't, s', ytitle = 'I, Amperes')
Igraph = gcurve(gdisplay=current, color = color.yellow)
# constants and initialization
emf = 3
# capacitance
C = 1
# resistance
R = 15
# charge
Q = 0
# time parameters
dt = 0.01
t = 0

# dynamics loop
while t < 150:
    rate(300)
    ##### PUT PHYSICS HERE #####################
    # calculate charge
    
    # cumulative value of charge
    
    # plot charge
    Qgraph.plot(pos=(t,Q))
    # calculate current
    
    ##### PUT PHYSICS HERE #####################
    # plot current
    Igraph.plot(pos=(t,I))
    # update time
    t += dt






    
    
