import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# 2
x0 = 0.2
N = 10

fig, axes = plt.subplots(2, 3, figsize=(10, 6))
axes = axes.ravel()

x = np.zeros(N+1)
x[0] = x0
for i, r in enumerate([0.1, 0.2, 0.5, 0.7, 0.9, 1]):
    for n in range(N):
        x[n+1] = r * x[n] * (1 - x[n])

    n = np.arange(N+1)
    ax = axes[i]
    ax.plot(n, x, label=f'r={r}', marker='o')
    ax.set_xlabel('n')
    ax.set_ylabel('x_n')
    ax.grid(True)
plt.tight_layout()
plt.show()

# 3
x0 = 0.2
N = 10

fig, axes = plt.subplots(2, 3, figsize=(10, 6))
axes = axes.ravel()

for i, r in enumerate([2.01, 2.25, 2.5, 2.75, 2.99]):
    x = np.zeros(N + 1)
    x[0] = x0
    for n in range(N):
        x[n + 1] = r * x[n] * (1 - x[n])

    ax = axes[i]

    n = np.arange(N + 1)

    even_idx = n[::2]
    odd_idx = n[1::2]
    x_even = x[::2]
    x_odd = x[1::2]
    x_star = 1 - 1/r
    ax.plot(even_idx, x_even, 'bo-', label='x_{2n}')
    ax.plot(odd_idx, x_odd, 'ro-', label='x_{2n+1}')
    ax.axhline(y=x_star, color='green', linestyle='--')
    ax.set_xlabel('n')
    ax.set_ylabel('x_n')
    ax.grid(True)
plt.tight_layout()
plt.show()

# 4

x0 = 0.2
n_steps = 50

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
axes = axes.ravel()

for i, r in enumerate([0.5, 1, 1.5, 27 / (2 * (7 * sqrt(7) - 10))]):
    xs = [x0]
    for _ in range(n_steps):
        x = xs[-1]
        xs.append(r * x * (1 - x) * (2 + x))

    n = list(range(len(xs)))
    ax = axes[i]
    ax.plot(n, xs, marker='o')
    ax.set_xlabel("n")
    ax.set_ylabel(r"$x_n$")
    ax.set_title(fr"$r = {r:.4f}$")
    ax.grid(True)

plt.tight_layout()
plt.show()
