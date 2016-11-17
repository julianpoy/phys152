#
# E field of a rod
#
from visual import *
# set up scene
scene.width=1024
scene.height=768
scene.background = color.white

#constants
epsilon=9e9
L=.6
N=7
# charge
Q=12e-9
scalefactor=.2e-3
deltay = L/N
# fractional point charge
deltaQ = Q/N

#set up rod and initial values
rod = cylinder(pos=(0,-L/2,0), axis=(0,L,0), radius=L/60, color=(1,.5,.5))
axis=curve(color=color.black,pos=[(0,-L,0),(0,L,0)])

#create "point charges" - simulate rod as a series of spheres
scene.mouse.getclick()

y = -L/2+deltay/2

# set up spheres loop
while y < L/2:
    a=sphere(pos=vector(0,y,0), radius=L/(2*N), color=color.red)
    y += deltay

# setup Enet visualization
# observe the E field at a location    
obslocation = vector(.2,.0,0)
# initialize Enet
Enet = vector(0,0,0)
# arrow from charge to observer location
ra = arrow(color=color.green, axis=(0,0,0), shaftwidth=L/60.)
# arrow for "local" E field due to a specific additive charge
dEa = arrow(pos=obslocation, color=color.orange, axis=(0,0,0), shaftwidth=L/60., fixedwidth=1)
# total "local" E field due to additive charges
Ea = arrow(pos=obslocation, axis=(0,0,0), color=color.blue,  shaftwidth=L/60., fixedwidth=1)

scene.mouse.getclick()

# dynamics loop
y = -L/2+deltay/2

while y < L/2:
    rate(5)
    ##### PUT PHYSICS HERE #####################
    # calculate E from the "point" sources


    
    ##### PUT PHYSICS HERE #####################
    # scale contribution from charge
    dEa.axis=deltaE*scalefactor # arrow for "local" E field due to a specific additive charge
    # arrow for previous "local" E field due to a specific additive charge
    dEa2 = arrow(pos=obslocation, axis=deltaE*scalefactor, shaftwidth=L/80, color=color.cyan)
    # calculate Enet
    Enet += deltaE
    # visualize Enet with arrow
    Ea.axis=Enet*scalefactor
 
##  
    y += deltay
    scene.mouse.getclick()

# visible is not true (0) - not displayed    
dEa.visible=0
ra.visible=0

print(' N=',N, 'mag(Enet)=',mag(Enet),'Enet = ',Enet)

