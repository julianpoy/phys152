#
# B field of a charge in motion
#
from visual import *
# set up scene
scene.background=color.white
scene.x = scene.y = 0
scene.width = 800
scene.height = 600

# constants
mzofp = 1e-7
L = 2e-10
# set up particle that will be moving - note charge on it (q)
particle = sphere(pos=(-1e-10,0,0), v = vector(2e5,0,0), q=1.6e-19,
                  radius=3e-12, color=color.red)
# time and scale
dt = 1e-18
Bscale = 12e-12  

# set up list of observation locations
olist = []
orad = 0.3e-10
for x in arange(-L/2, L/2, L/8):  
    for theta in arange(0,2*pi,pi/4):
        olist.append(arrow(pos=(x, orad*cos(theta), orad*sin(theta)),
                axis=(0,0,0),color=color.cyan))

# move proton, calculate B field at each position       
dt = 1e-18
scene.autoscale = 0
# dynamic loop - particle in motion
particle.x = -L/2
while particle.x < L:
    rate(100)
    ##### PUT PHYSICS HERE #####################
    # update position of particle
    
    # calculate B field for each location around the charge
    for barrow in olist:
        
        barrow.axis = B*Bscale
    ##### PUT PHYSICS HERE #####################

scene.mouse.getclick()
# static view at a particular location
particle.x = 0
for barrow in olist:
    r = barrow.pos - particle.pos
    B = mzofp*particle.q*cross(particle.v, norm(r))/mag(r)**2
    barrow.axis = B*Bscale

            
