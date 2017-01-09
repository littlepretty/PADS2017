import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=18)

bs_data = np.loadtxt('bs_emu_resource.txt')
tree_data = np.loadtxt('tree_emu_resource.txt')
bs_rules = bs_data[:, 2]
tree_rules = tree_data[:, 2]

width = 4
ticks = [10, 20, 30, 40, 50]
scale_tree = [x - width for x in ticks]
scale_bs = [x for x in ticks]

fig, ax = plt.subplots()
ax.bar(scale_tree, tree_rules, width, color='w', hatch='/',
       label='Tree Network')
ax.bar(scale_bs, bs_rules, width, color='w', hatch='\\',
       label='Big-Switch Network')
print(scale_tree)
print(scale_bs)

plt.yscale('log')
plt.xticks(ticks, ['(2,3)', '(2,4)', '(3,3)', '(3,4)', '(4,3)'])
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('Tree-Topology Network Settings')
plt.ylabel('Total #Rules in Log Scale')

plt.tight_layout()
# eps format doesn't support transparency
plt.savefig('comp_num_rules.eps', fmt='eps')
plt.show()
