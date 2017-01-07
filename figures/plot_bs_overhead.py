import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=18)

data = np.loadtxt('bs_overhead.txt')

x = data[:, 2]
y = data[:, 3]
logx = np.log2(data[:, 2])
logy = np.log2(data[:, 3])

print(x)
print(y)

fig, ax = plt.subplots()
ax.plot(logx, logy, 'b', linewidth=4.0, label='Binary logarithm')
width = 0.4
ax.bar(logx - width/2, logy, width, color='white', hatch='//')

plt.xticks(logx, ['%.1f' % i for i in logx])
plt.grid(True)

plt.xlabel('$\log_2$(#Rules Processed)')
plt.ylabel('$\log_2$(Runtime) (Milliseconds)')
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig('bs_overhead.eps', fmt='eps')
plt.show()
