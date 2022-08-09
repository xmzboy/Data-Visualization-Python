import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('seaborn')
fig,ax = plt.subplots()

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.RdBu, edgecolors='none', s=1)
ax.scatter(rw.x_values[0], rw.y_values[0], c='green', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='black', s=100)
plt.show()