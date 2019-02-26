import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

#read in a file
filenameToUse = "data_files\\b_should_be_easy.in"

#read in data
inputfile = open(filenameToUse,"r")
header = inputfile.readline().rstrip('\n').split(" ")
rows = int(header[0])
columns = int(header[1])


rides = []
x = []
y = []

x2 = []
y2 = []

#another to track earliest start and latest end timesteps
xEarliestStart = []
yLatestEnd = []

rideIndex = []


for line in inputfile:
    rides.append([int(x) for x in line.rstrip('\n').split(" ")])
inputfile.close()

space = [[0 for i in range(columns)] for j in range(rows)]


for i, r in enumerate(rides):
    x.append(r[0])
    y.append(r[1])
    x2.append(r[2])
    y2.append(r[3])
    xEarliestStart.append(r[4])
    yLatestEnd.append(r[5])
    rideIndex.append(i)
    space[r[0]][r[1]] += 1





# Create data
#N = 500
# x = np.random.rand(N)
#y = np.random.rand(N)
colors = (0,0,0)
colors2 = (10,0,0)
area = np.pi*3

# xS = []
# yS = []
# tS = []
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# for r in rides:
#     xS = [r[0],r[2]]
#     yS = [r[1],r[3]]
#     tS = [r[4],r[5]]
#     #plt.plot(xS, yS,tS '-o')
#     #plt.scatter(xS,yS, s=area, c='orange', alpha=0.5)
#     color = np.random.rand(3,)
#     ax.plot(x, y, xEarliestStart, c=color, marker='o')
# plt.show()

# create x-y points to be used in heatmap
# xnp = np.array(x)
# ynp = np.array(y)
# #znp = np.array(xEarliestStart)
#
#
# plt.imshow(space, cmap='hot', interpolation='nearest')
# plt.show()

# xi = np.linspace(xnp.min(), ynp.max(), 1000)
# yi = np.linspace(xnp.min(), ynp.max(), 1000)
#
# # Z is a matrix of x-y values
# zi = griddata((xnp, ynp),znp , (xi[None,:], yi[:,None]), method='cubic')
#
# # I control the range of my colorbar by removing data
# # outside of my range of interest
# # zmin = 3
# # zmax = 12
# # zi[(zi<zmin) | (zi>zmax)] = None
#
# # Create the contour plot
# CS = plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow)
# plt.colorbar()
# plt.show()

# Plot
plt.scatter(x, y, s=area, c='green', alpha=0.5, marker='<')
plt.scatter(x2, y2, s=area, c='red', alpha=0.5,marker='>')
plt.title('Ride start (green) and end (red) points')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#plt.clear()
plt.scatter(xEarliestStart, yLatestEnd, s=area, c='orange', alpha=0.5)
plt.title('Ride start (x) and end (y) times')
plt.xlabel('Start time')
plt.ylabel('End time')
plt.show()

#try a 3d graph with start time and start x,y
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
#for c, m, zlow, zhigh in [('r', 'o'), ('b', '^')]:

ax.scatter(x, y, xEarliestStart, c='red', marker='o')

ax.set_xlabel('Start X')
ax.set_ylabel('Start Y')
ax.set_zlabel('Time')

plt.show()

#plot the position of the ride with its start time- they may need to be SORTED
plt.scatter(rideIndex,xEarliestStart, s=area, c='orange', alpha=0.5)
plt.title('Index Position (x) and Start Time (y)')
plt.xlabel('Index in Ride List')
plt.ylabel('Start time')
plt.show()
