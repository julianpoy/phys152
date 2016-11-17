# Faraday's Law: bar magnet moves at constant velocity, then briefly comes to rest and reverses
# What happens in a superconductor ring?
from visual import *

# set up visualization parameters
showring = True # show ring if True, disk if False
showallB = True # if True, show B at many places, not just within circle
showE = True # show E along ring if True
show_dBdt = True # show magenta arrow for dB/dt

# set up scene
scene.height= 800
scene.width = 800
scene.x = scene.y = 0
scene.background = color.white
##scene.lights = [0.7*norm(vector(1,0,.5)), 0.7*norm(vector(-1,0.5,0.5))]

scene.center = vector(0.2,0,0)
scene.forward = -vector(1,0,2.5)
scene.autoscale = 0
scene.range = (0.6,0.6,0.6)
# set up colors
Bcolor = (0,.5,.5) # bluegreen
Bcolorother = (.8,1,1)
sw = 0.01
swother = 0.005
# set up a function to do some B field calculations
def Bfield(source,obsloc):
    r = source-obsloc
    return kmag*(3*dot(mu,norm(r))*norm(r) - mu)/mag(r)**3 #### physics ####
# set up a function to do some B field arrow axis calculations
def showB():
    for arr in Bother:
        arr.axis=Bscale*Bfield(magnet.pos, arr.pos)
# initialize parameters
xhat = vector(1,0,0)

Rdisk = 0.3
f = cos(pi/4.)
rmagnet = 0.03
Lmagnet = 0.12
dpole = 0.03
# define a frame to make a composite object: (group the "magnet" objects)
magnet = frame(pos=(0,0,0))
# construct the magnet as a set of grouped objects
south = cylinder(frame=magnet, pos=(-Lmagnet/2,0,0), radius=rmagnet, color = (0,0,1),
              axis=(dpole,0,0))
north = cylinder(frame=magnet, pos=(Lmagnet/2,0,0), radius=rmagnet, color = (1,0,0),
              axis=(-dpole,0,0))
bar = cylinder(frame=magnet, pos=south.pos+vector(dpole,0,0), radius=south.radius,
                  axis = north.pos-vector(dpole,0,0)-south.pos-vector(dpole,0,0), color=(0.7,0.7,0.7))
# If showring True then display the ring else display a surface
# move the position of the ring: pos=vector(0.4,0,0) try (0.6,0,0) (0.2,0,0)
if showring:
    surface = ring(pos=vector(0.4,0,0), radius=Rdisk, thickness=0.001)
    surface.center = surface.pos
else:
    surface = cylinder(pos=vector(0.4,0,0), radius=Rdisk, axis=(0.002,0,0), color=(0.8,0.8,0.8))
    surface.center = surface.pos+surface.axis/2

deltax = Lmagnet/5
kmag = 1e-7
mu = vector(1.0,0,0) # magnetic dipole moment of bar magnet

#B = Bfield(magnet.pos, surface.pos) # typical 2e-6 tesla
# define scales and location
Bscale = 0.13*Rdisk/2e-6
Escale = 0.7*Rdisk/2e-7
xmax = 0.4*Rdisk

#E on perimeter of ring (surface)- arrows are organge
Earr=[]
for theta in arange(0,2*pi,pi/6):
    a=arrow(pos=(surface.center.x, surface.radius*cos(theta),surface.radius*sin(theta)),
                           axis=(0,0,0), color=color.orange, shaftwidth=.01)
    a.vv = norm(a.pos - surface.pos)
    a.visible = showE
    Earr.append(a)
## arrows on surface (ring) at which to calculate magnetic field, flux
Bsurface = []
dR = 0.4*Rdisk
for y in arange(-Rdisk+dR,Rdisk-dR*0.9,dR):
    a = arrow(pos=(surface.center.x, y, 0),axis=(0,0,0),
              color=Bcolor, fixedwidth=1, shaftwidth=sw)
    Bsurface.append(a)

## locations at which to display magnetic field around magnet
Bother = []
dtheta = pi/6
##phi = pi/4
for theta in arange(dtheta, 2*pi-dtheta/2, dtheta):
    x = Rdisk*cos(theta)
    y = Rdisk*sin(theta)
    z = 0
    Bother.append( arrow(pos=(x,y,z), axis=(0,0,0)) )
# arrow parameters
for arr in Bother:
    arr.color = Bcolorother
    arr.shaftwidth = swother
    arr.fixedwidth = 1
# initialize
flux = 0
dt = 0.01
t = 0
vx = v0 = 0.1

## dB/dt calculation
##dBdtarr = arrow(pos=surface.pos+vector(0,-0.1*Rdisk,0.2*Rdisk), axis=(0,0,0), color=color.magenta,
##                fixedwidth=1, shaftwidth=sw)
##if show_dBdt:
##    dBdtarr.visible = 1
##else:
##    dBdtarr.visible = 0

# motion dynamics loop - do forever    
while 1:
    rate(1/dt)
    t = t + dt
    # magnet location on x axis
    if abs(magnet.pos.x+vx*dt) > 0.7*xmax:
        if magnet.pos.x > 0:
            ax = -0.2
        else:
            ax = 0.2
    else:
        ax = 0
        if vx > 0:
            vx = v0
        else:
            vx = -v0

    # magnet velocity
    
    vx += #### PHYSICS
    
    # magnet position
    
    magnet.pos.x += #### PHYSICS
    
    # display control- if true show the field
    if showallB: showB()
    oldflux = flux
    # calculations on the surface (B field)
    flux = 0
    for arr in Bsurface:
        B = Bfield(magnet.pos, arr.pos)
        arr.axis = B*Bscale
        
        flux += #### PHYSICS
        
    # update flux
    dflux = flux - oldflux
    
    ## dB/dt calculation visualization
    ##dBdtarr.axis = (0.15*dflux/1e-8,0,0)
    
    # calculate E field
    
    E = #### PHYSICS
    
    # update display for E field on the disk
    for a in Earr:
        a.axis = -E*Escale*cross(xhat,a.vv)
    

