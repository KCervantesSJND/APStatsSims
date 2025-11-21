import numpy as np
import matplotlib.pyplot as plt

# Set up rng
rng = np.random.default_rng()

# Simulate 7 cars
# 16% of them fail smog check
n = int(1E7)
samp = rng.random((7, n))
samp = (samp > 0.16).all(axis=0)

# get relative frequencies
x = np.arange(n) + 1
y = np.cumsum(samp) / x

# plot relative frequencies
fig, ax = plt.subplots()
ax.hlines(0.84 ** 7, x[0], x[-1], color = 'tab:orange')
ax.plot(x, y)
ax.set_title('All 7 Cars Pass Smog Check')
ax.set_xlabel('Number of Trials')
ax.set_xscale('log', base = 10)
ax.set_ylabel('Relative Frequency')
plt.savefig('car.png')