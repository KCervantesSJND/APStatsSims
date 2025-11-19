import numpy as np
import matplotlib.pyplot as plt

# Set up rng
rng = np.random.default_rng()

# Simulate Rolling Dice
n = int(1E7)
samp = (
    rng
    .integers(1, 7, (2, n))
    .sum(axis=0)
)

# get relative frequencies
x = np.arange(n) + 1
y = np.cumsum(samp == 7) / x

# plot relative frequencies
fig, ax = plt.subplots()
ax.hlines(1 / 6, x[0], x[-1], color = 'tab:orange')
ax.plot(x, y)
ax.set_title('Rolling a 7')
ax.set_xlabel('Number of Trials')
ax.set_xscale('log', base = 10)
ax.set_ylabel('Relative Frequency')
plt.savefig('dice7.png')
