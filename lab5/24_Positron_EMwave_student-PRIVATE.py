# charged particle interaction with a sinusiodal EM field (light) 
#
from __future__ import print_function, division
### DO NOT MAKE THIS FILE PUBLIC ###
from visual import *
print("Solution to homework problem.")
# set up the scene
scene.width=1000
scene.height=600
scene.x = scene.y = 0
#scene.background = color.white
# initialize some parameters
c = 3e8
# lambda and omega
lamb = 600
omega = 2*pi*c/lamb
sw = lamb/40.
# set up positions for visualization of EM field
xx = arange(-2*lamb,2.0001*lamb,lamb/20.)
# set up visualization arrows for electromagnetic field (light)
xhat = vector(1,0,0)
Evec = []
Bvec = []
for x in xx:
    # E field
    ea = arrow(pos=(x,0,0), axis=(0,lamb/10.,0), color=(1.,.6,0),
               shaftwidth=sw)
    # B field
    ba = arrow(pos=(x,0,0), axis=(0,0,0), color=(0,1,1),
               shaftwidth=sw)
    ea.B = ba
    Evec.append(ea)
# initialize
t = 0.
dt = lamb/c/900.
E0 = 1.0e4
# scaling
escale = lamb/E0
fscale = lamb/(2*1e-15)
# charge positive for positron, negative for electron
pq= 1.6e-19
# set up a positron
positron = sphere(pos=(-2*lamb,0,0), radius=lamb/25., color=color.red,
                m = 9e-31, p=vector(0,0,0), q=pq)   #p=vector(0,0,0.1e-21)
# set up an electron visualization
if positron.q < 0:
    positron.color=color.blue
# set up arrows for particle     
positron.visible = 1
positron.trail = curve(color=positron.color, radius=4.5)
positron.F = arrow(pos=positron.pos, axis=(0,0,0), color=color.green,
                   shaftwidth=sw)
# initialize velocity
v = vector(0,0,0)

scene.autoscale = 0
flag = 0
t = 0
# dynamic loop - run forever
while 1:
    rate(200)
    t = t+dt
    # calculate E field axis dimensions
    for ea in Evec:
       ea.axis = (0,(E0*escale)*cos(omega*t - 2*pi*ea.x/lamb),0)
       ea.B.axis = cross(xhat, ea.axis)*.7
    # calculate E and B vector location   
    nn = E0*cos(omega*t - 2*pi*positron.x/lamb)
    E = vector(0,nn,0)
    B = vector(0,0,nn/c)
    # force from E field
    Fe = #### PHYSICS
    
    # force from B field
    Fb = #### PHYSICS
    
    # calculate force axis dimension
    positron.F.axis = (Fe+Fb)*fscale
    # calculate force position so the arrow tracks the particle motion
    positron.F.pos = positron.pos
    # calcuate momentum (MOMENTUM PRINCIPLE)
    positron.p = #### PHYSICS
    
    # velocity
    v = #### PHYSICS
    
    # particle position
    positron.pos = #### PHYSICS
    
    # visualize previous motion of particle
    positron.trail.append(pos=positron.pos)
