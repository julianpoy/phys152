#
# motion of proton (+ charge) in a di-pole E field of charge q and -q
#
from visual import *
from visual.graph import *

s = 0.2e-9
# di-pole charges
q1 = sphere(pos=(-s/2,0,0), q = -1.6e-19, radius=s/10, color=color.red)
q2 = sphere(pos=(s/2,0,0),  q =  1.6e-19, radius=s/10, color=color.blue)

# proton
proton = sphere(pos=( -0.1e-9,0.3e-9,0), q = 1.6e-19, m = 1.67e-27,
                v = vector (0,0,0), radius=s/20, color=color.yellow,make_trail=True)
# proton momentum = proton mass * proton velocity
proton.p = proton.m * proton.v

epsilon = 9e9
# time initialization
t = 0
dt = 1.e-18

## graphic output for energy
##
##graph_energy = gdisplay(x=500,y=0,width=400, height=400,
##                 title="energy",
##                 xtitle="t (s)",
##                 ytitle="E (J)",
##                 background=color.white)
##
##U_graph=gcurve(gdisplay=graph_energy,color=color.magenta)
##K_graph=gcurve(gdisplay=graph_energy,color=color.cyan)
##E_graph=gcurve(gdisplay=graph_energy,color=color.white)
##
## graphic output for work-energy
graph_work = gdisplay(x=500,y=500,width=400, height=400,
                 title="work - energy",
                 xtitle="t (s)",
                 ytitle="E (J)",
                 background=color.white)
# associate curves for output
W_graph=gcurve(gdisplay=graph_work,color=color.red)
K2_graph=gcurve(gdisplay=graph_work,color=color.blue)

work = 0

scene.mouse.getclick ()
# dynamics loop 
while t < 500000*dt :
    rate(100000)
    ##### PUT PHYSICS HERE #####################
    # calculate E field
    
    # work
    

##    U1 = epsilon*proton.q*q1.q/r1
##    U2 = epsilon*proton.q*q2.q/r2
##
##    U = U1 + U2
    
    # kinetic energy
    

##    E = K + U
##
##    U_graph.plot(pos=(t,U))
##    K_graph.plot(pos=(t,K))
##    E_graph.plot(pos=(t,E))
        ##### PUT PHYSICS HERE #####################
    
    # plot output
    W_graph.plot(pos=(t,work))
    K2_graph.plot(pos=(t,K))

    # time update
    t +=  dt

    # stop if path collides with charge
    if(mag(proton.pos-q1.pos) < q1.radius or mag(proton.pos-q2.pos) < q2.radius ) :
        break
    


    
