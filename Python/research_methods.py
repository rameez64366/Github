# All units in (m, Kg, s)
LENGTH = 5
WIDTH = 2.5
DEPTH = 0.1
RADIUS = 0.5
NUM = 3

E = 2e11
NU = 0.27

PRESSURE = 1000

from ansys.mapdl.core import launch_mapdl
mapdl = launch_mapdl()

mapdl.clear()
mapdl.prep7()
mapdl.block(0, LENGTH, 0, WIDTH, 0, DEPTH)
for i in range(1,NUM+1):
    mapdl.cyl4(i*LENGTH/(NUM+1),WIDTH/2,RADIUS,'','','',2*DEPTH)
mapdl.vsbv(1,'all')
mapdl.vplot('all')