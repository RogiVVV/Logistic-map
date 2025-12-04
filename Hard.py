import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# 1

x0 = 0.2
n_steps = 50

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
axes = axes.ravel()

for i, r in enumerate([3, 3.2, 3.5, 3.5699456]):
    xs = [x0]
    for _ in range(n_steps):
        x = xs[-1]
        xs.append(r * x * (1 - x))

    n = list(range(len(xs)))
    ax = axes[i]
    ax.plot(n, xs, marker='o')
    ax.set_xlabel("n")
    ax.set_ylabel(r"$x_n$")
    ax.set_title(fr"$r = {r:.4f}$")
    ax.grid(True)

plt.tight_layout()
plt.show()


# 2
def lamerey_staircase(r, x0=0.2, n_steps=50):
    # логистическое отображение
    def f(x):
        return r * x * (1 - x)

    # подготовим точки для графика функции и диагонали
    xs = np.linspace(0, 1, 400)
    fx = f(xs)

    plt.figure(figsize=(6, 6))
    plt.plot(xs, fx, 'k', label=r'$y = f(x)$')   # кривая отображения
    plt.plot(xs, xs, 'r--', label=r'$y = x$')    # диагональ

    # строим лестницу
    x, y = x0, 0
    for _ in range(n_steps):
        # вертикально: (x, y) -> (x, f(x))
        y_new = f(x)
        plt.plot([x, x], [y, y_new], 'b')
        # горизонтально: (x, f(x)) -> (f(x), f(x))
        plt.plot([x, y_new], [y_new, y_new], 'b')
        x, y = y_new, y_new  # переносим точку на диагональ

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel(r'$x_n$')
    plt.ylabel(r'$x_{n+1}$')
    plt.title(fr'Лестница Ламерея, r = {r}')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', 'box')
    plt.tight_layout()
    plt.show()


for r in [2.9, 3, 3.5, 3.5699456]:
    lamerey_staircase(r=r, x0=0.2, n_steps=30)
'''Вывод:
При неподвижной точке образуется спираль,
При цикле из двух точек образуется две спирали, значения чередуются
При цикле из 4+ точек образуется ещеё более сложная конструекция
При r = 3.5699456... график хаотичен'''

# 3
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

'''
Вывод: впринципе прослеживается сходство с логистическим отображением,
но так как это другая функция с разными областями значений для r,
r_{\infty} у них отличаются
'''