#
# B field of a ring
#
from visual import *

# set up scene
scene.width = scene.height = 600
scene.x = scene.y = 0
scene.background = color.white
# set up axes for display
def axes(a):
    axes=curve(pos=[(-a,0,0),(a,0,0),(0,0,0),(0,-a,0),(0,a,0),(0,0,0),
                    (0,0,-a),(0,0,a)], color=(0.7,0.7,0.7))
    scene.autoscale = 0
# get axes
axes(0.1)

# current
I = 1.0
# constants
kmag = 1e-7
bscale = 1e5

#set up loop
R = 0.01
loop = ring(pos=(0,0,0), axis=(1,0,0), radius=R, thickness=0.001)

# list of ordered objects - locations on the loop
locations = []
# set up field display arrows oriented around the ring
# arange creates an array of numbers for locating arrows
dtheta = pi/6.
Ro = 6*R
for theta in arange(0, pi+dtheta, dtheta):
    x = Ro*cos(theta)
    y = Ro*sin(theta)
    z = 0
    locations.append((x,y,z))
    locations.append((x,-y,z))


# list of ordered objects -observer locations
obs1 = []
# put arrows at prescribed locations
for point in locations:
    obs1.append(arrow(pos=point, axis=(0,0,0), color=color.cyan,
                      shaftwidth=0.003))

dphi = pi/20.
# calculate B field for the arrow axis length
for barrow in obs1:
    B = vector(0,0,0)
    for phi in arange(0,2*pi,dphi):
        # locations on ring
        a = vector(0,R*cos(phi), R*sin(phi))
        b = vector(0,R*cos(phi+dphi), R*sin(phi+dphi))
        ##### PUT PHYSICS HERE #####################
        # delta length of wire contributing to B field
        
        # calculate B field section 18.8
        
        # superposision
        
        ##### PUT PHYSICS HERE #####################
    # arrow for all the ring increments at the observer location
    barrow.axis = B*bscale

