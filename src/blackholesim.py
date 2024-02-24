from libs.simulationequations import *

binit = 1
bfinal = 5
ncurves = 10

for i in range(ncurves):
    plt.plot(*generate_trajectory(1,3, i*(bfinal-binit)/ncurves + binit, 100), 'b')

plt.xlim([-5,5])
plt.ylim([-5,5])
ax = plt.gca()
ax.set_aspect(1)
ax.add_patch(plt.Circle((0,0), 2, color ='k', zorder=10))

plt.show()
