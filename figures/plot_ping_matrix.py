import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker

matplotlib.rc('font', size=18)

depth = 2
fanout = 3
tree_matrix = np.loadtxt('ping_matrix_%d_%d.txt' % (depth, fanout))
bs_matrix = np.loadtxt('bs_ping_matrix_%d_%d.txt' % (depth, fanout))
ticks = [str(x) for x in range(0, len(tree_matrix) + 1)]

fig, ax = plt.subplots()
cax = ax.matshow(tree_matrix, cmap=plt.cm.gray)
fig.colorbar(cax)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax.set_xticklabels(ticks)
ax.set_yticklabels(ticks)
plt.xlabel('Destination Hosts')
plt.ylabel('Source Hosts')
plt.tight_layout()

plt.savefig('ping_mat_%d_%d.pdf' % (depth, fanout), format='pdf')
plt.show()

fig, ax = plt.subplots()
cax = ax.matshow(bs_matrix, cmap=plt.cm.gray)
fig.colorbar(cax)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax.set_xticklabels(ticks)
ax.set_yticklabels(ticks)
plt.xlabel('Destination Hosts')
plt.ylabel('Source Hosts')
plt.tight_layout()

plt.savefig('bs_ping_mat_%d_%d.pdf' % (depth, fanout), format='pdf')
plt.show()
