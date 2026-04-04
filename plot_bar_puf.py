import matplotlib.pyplot as plt
import numpy as np

num_devices = [1, 2, 4, 6, 8] 
configs = ['Private Blockchain', 'Public Blockchain', 'Hybrid Blockchain']
response_times = np.array([
    [0.004736, 0.13782, 1.11165, 1.913988889, 2.982029167],
    [0.006806667, 0.133246667, 0.976041667, 2.105966667, 2.889304167],
    [0.00707, 0.1571, 0.956841667, 2.163422222, 2.840539583]
])

errors = np.array([
    [0.000192007, 0.007816979, 0.123772961, 0.122651733, 0.133972925],
    [0.000354059, 0.006746472, 0.06851639, 0.094959898, 0.047256618],
    [0.000395334, 0.022621818, 0.048645905, 0.197207968, 0.133173261]
])

# Bar width and positions
x = np.arange(len(num_devices))  # the label locations
width = 0.25                     # width of each bar

fig, ax = plt.subplots()

# Plot each configuration
for i, (config, rt, err) in enumerate(zip(configs, response_times, errors)):
    ax.bar(x + i*width, rt, width, yerr=err, capsize=5, label=config)

# Labels and title
ax.set_xticks(x + width)  # center xticks between grouped bars
ax.set_xticklabels(num_devices)
ax.set_xlabel('Number of Connected IoT Devices')
ax.set_ylabel('Average Request Completion Time (seconds)')
ax.legend()

plt.tight_layout()
plt.savefig('puf_bar_resp')
