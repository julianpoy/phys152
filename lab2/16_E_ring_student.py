#
# E field of a ring
#
from visual import *
# set up scene
scene.background = color.white
scene.width=1024
scene.height=768
# set up axes for display 
def axes(aa):
    axes=curve(pos=[(-aa,0,0),(aa,0,0),(0,0,0),(0,-aa,0),(0,aa,0),(0,0,0),
                    (0,0,-aa),(0,0,aa)], color=color.black)
    scene.autoscale = 1
aa = 6
# get axes
axes(aa)

# create a ring
a_ring = ring(pos=(-5,0,0), radius=3, color=color.red, thickness=0.05)

N = 5
# observer location
obsloc = vector(2,2,0)
# arrow for net E field direction and magnitude
Enet = arrow(pos=obsloc, axis=(0,0,0), shaftwidth=0.03, color=color.magenta, visible=1, fixedwidth=1)
dtheta=pi/N
angles = arange(0,2*pi,dtheta)

epsilon = 9e9
# charge
Q = 20e-9
# partial charge at each location on ring
dQ = Q/N

scene.mouse.getclick()
# point charge location on ring
ring_piece = sphere(pos=(-5,a_ring.radius,0), color=color.blue, radius=a_ring.thickness*2)
# arrow from point ring charge to observer location
ra = arrow(pos=ring_piece.pos, axis=(0,0,0),color=color.green, shaftwidth=0.05, fixedwidth=1)

for theta in angles:
    ##### PUT PHYSICS HERE #####################
    
    ##### PUT PHYSICS HERE #####################
    # cumulative E field due to fractional ring charges
    Enet.axis += dE.axis
    ####print (theta/pi*180)
    scene.mouse.getclick()

scene.mouse.getclick()
# visible is not true (0) - not displayed
ra.visible = 0
ring_piece.visible = 0


#Enet.visible=1



